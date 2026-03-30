import socket
from colorama import *
import os
from datetime import datetime
import json
import threading
import sqlite3
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import bcrypt

dataFolder = os.sep.join([os.path.split(__file__)[0], # Obtient le chemin absolus de `game.py`
                        '..', # Remonte d'un répertoir (Répertoir source)
                        'data'
                    ])

class loggeur() :
    def __init__(self):

        self.hour = None
        self.file = None
        self.update_file()

    def update_file(self) :
        now = datetime.now()
        if self.hour != now.strftime("%H") :

            folder_path = now.strftime("logs/%Y/%m/%d")

            folder_path = self.asset_doc = os.sep.join([dataFolder, # Dossier data
                                                            'logs',
                                                            now.strftime("%Y"), # Anée
                                                            now.strftime("%m"), # mois
                                                            now.strftime("%d") # Jour
                                                        ])

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_name = now.strftime("log_%H.log")
            chemin_fichier_log = os.path.join(folder_path, file_name)
            self.file = open(chemin_fichier_log, 'a')

    def format(self, type, string) :
        now = datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        return f"[{time}] [{type}] : {string}\n"

    def error(self, message) :
        message = self.format("ERROR", message)
        self.file.write(message)
        print(Fore.RED, message, Fore.RESET, sep="", end="")

    def warn(self, message) :
        message = self.format("WARN", message)
        self.file.write(message)
        print(Fore.YELLOW, message, Fore.RESET, sep="", end="")

    def log(self, message) :
        message = self.format("INFO", message)
        self.file.write(message)
        print(message, end="")

class Serveur:
    def __init__(self):
        self.handlers = {}
        self.clients = []

    def on(self, msg_type):
        def decorator(func):
            self.handlers[msg_type] = func
            return func
        return decorator

    def dispatch(self, message, client_socket, aes_key):
        handler = self.handlers.get(message["type"])
        if handler:
            handler(message, client_socket, aes_key)

_local = threading.local()

def get_conn(): # By claude.ai
    if not hasattr(_local, "conn"):
        _local.conn = sqlite3.connect(os.sep.join([dataFolder, "ecopixel.db"]))
        _local.conn.row_factory = sqlite3.Row  # accès par nom de colonne
    return _local.conn

def get_cursor(): # By claude.ai
    return get_conn().cursor()

def save_game() :
    pass

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key().public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo
)

OAEP = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)

def aes_decrypt(aes_key, iv, data):
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    decrypteur = cipher.decryptor()
    données = decrypteur.update(data) + decrypteur.finalize()
    pad = données[-1]
    return données[:-pad]


log = loggeur()
s = Serveur()

log.log(f'Script start')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try :
    config_file = open(os.sep.join([dataFolder, "json", "config.json"]))
    config = json.load(config_file)
except FileNotFoundError :
    log.warn("Config file doesn't exsist. Use default config")
    config = {}

server.bind((config.get("HOST", "0.0.0.0"), config.get("PORT", 2123)))
server.listen(5)

log.log(f'Serveur start on {server.getsockname()[0]}:{server.getsockname()[1]}')

@s.on("login")
def login(message, client_socket, aes_key) :

    if message["username"].strip() == "" or message["password"].strip() == "":
        message = {
            "type": "login",
            "response_type": "error",
            "message": "Username or password empty"
        }
        send(client_socket, aes_key, message)

    else :

        username = message['username']
        password = message['password']

        cursor = get_cursor()
        cursor.execute("SELECT * FROM players WHERE username = ?", (username,))
        player = cursor.fetchone()
        if player is not None :
            id_player, username, savePassword, x, y, money, sprout, fertilizer, fruits, arrosoir = player
            if bcrypt.checkpw(password.encode('utf-8'), savePassword.encode('utf-8')):
                if os.path.exists(os.sep.join([dataFolder, "data_game.json"])) :
                    gamedata = open(os.sep.join([dataFolder, "data_game.json"]), 'r')
                    gamedata = json.load(gamedata)
                else :
                    gamedata = {}
                send(client_socket, aes_key, {
                    "type": "login",
                    "response_type" : "succes",
                    "player_data" : {
                        "username" : username,
                        "x" : x,
                        "y" : y,
                        "money": money,
                        "sprout": sprout,
                        "fertilizer": fertilizer,
                        "fruits": fruits,
                        "arrosoir": arrosoir
                    },
                    "gamedata" : gamedata
                })
            else :
                send(client_socket, aes_key, {
                    "type": "login",
                    "response_type" : "error",
                    "message" : "Mauvais mot de passe"
                })

        else :

            salt = bcrypt.gensalt()

            # Hacher le mot de passe
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
            cursor.execute("insert into players ('username', 'password') values (?, ?)", (username,hashed_password))
            send(client_socket, aes_key, {
                "type": "login",
                "response_type" : "succes",
                "player_data" : {
                    "username" : username
                }
            })

        get_conn().commit()

def handle_client(client_socket, address):
    buffer = ""
    aes_key = None
    try :
        while True:
            if aes_key is None :
                chunk = client_socket.recv(4096).decode('utf-8')
                if not chunk:
                    break
                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    data = json.loads(line)
                    log.log(f"New message receive by {address[0]}:{address[1]}")
                    if data["type"] == "init" :
                            compatible_version = ['1']
                            if data['version'] in compatible_version :

                                message = {
                                    "type": "init",
                                    "accept" : True,
                                    "public_key": base64.b64encode(public_key).decode()
                                }

                                json_message = json.dumps(message) + "\n"
                                client_socket.sendall(json_message.encode('utf-8'))

                                aes_key = client_socket.recv(256)
                                aes_key = private_key.decrypt(aes_key, OAEP)

                            else :
                                message = {
                                    "type": "init",
                                    "accept" : False
                                }

                                json_connexion_message = json.dumps(message) + "\n"
                                client_socket.sendall(json_connexion_message.encode('utf-8'))
            else :
                entête = client_socket.recv(4)
                if not entête:
                    break
                taille = int.from_bytes(entête, "big")
                paquet = client_socket.recv(taille)
                iv = paquet[:16]
                données_chiffrées = paquet[16:]
                chunk = aes_decrypt(aes_key, iv, données_chiffrées).decode("utf-8")

                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    data = json.loads(line)
                    log.log(f"New message receive by {address[0]}:{address[1]}")
                    s.dispatch(data, client_socket, aes_key)
    except ConnectionResetError :
        pass
    try:
        client_socket.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    client_socket.close()

players = []
server.settimeout(1.0)

def aes_encrypt(aes_key, message: bytes) -> bytes:
    iv = os.urandom(16)
    # Padding PKCS7
    pad = 16 - len(message) % 16
    pad_message = message + bytes([pad] * pad)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encrypter = cipher.encryptor()
    encrypt_data = encrypter.update(pad_message) + encrypter.finalize()
    return iv + encrypt_data

def send(client_socket, aes_key, data: dict):
    message = (json.dumps(data) + "\n").encode("utf-8")
    paquet = aes_encrypt(aes_key, message)
    client_socket.sendall(len(paquet).to_bytes(4, "big") + paquet)

try :
    while True:
        try :
            client_socket, address = server.accept()
        except socket.timeout:
            continue
        log.log(f"New connection of {address[0]}:{address[1]}")
        players.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.daemon = True
        thread.start()
except KeyboardInterrupt :
    log.log("Close server by user")
except OSError as e:
    log.error(f"Close server by OSError : {e}")
except Exception as e :
    log.error(f"Close server by {e} error")
finally :
    server.close()
