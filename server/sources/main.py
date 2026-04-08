import socket
from colorama import *
import os
from datetime import datetime
import json
import threading
import base64
import bcrypt
from sqlalchemy import create_engine, text, bindparam
import encrypt as encr
import log

dataFolder = os.sep.join([os.path.split(__file__)[0], # Obtient le chemin absolus de `game.py`
                        '..', # Remonte d'un répertoir (Répertoir source)
                        'data'
                    ])

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

"""
_local = threading.local()

def get_conn(): # By claude.ai
    if not hasattr(_local, "conn"):
        _local.conn = sqlite3.connect(os.sep.join([dataFolder, "ecopixel.db"]))
        _local.conn.row_factory = sqlite3.Row  # accès par nom de colonne
    return _local.conn

def get_cursor(): # By claude.ai
    return get_conn().cursor()

"""

engine = create_engine("sqlite:///" + os.sep.join([dataFolder, "ecopixel.db"]), pool_size=5, max_overflow=10)
    
def save_game() :
    pass

connected = {}

log = log.loggeur(dataFolder)
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

def send(client_socket, aes_key, data: dict):
    message = (json.dumps(data) + "\n").encode("utf-8")
    paquet = encr.aes_encrypt(aes_key, message)
    client_socket.sendall(len(paquet).to_bytes(4, "big") + paquet)

def send_all_player(message:dict, ignore=None) :
    for socket, player in list(connected.items()) :
        if socket != ignore:
            try:
                send(socket, player["aes_key"], message)
            except OSError:
                pass

@s.on("start_move")
@s.on("stop_move")
@s.on("pos")
def player_move(message, client_socket, aes_key) :
    message['username'] = connected[client_socket]["username"]
    send_all_player(message, client_socket)


def login_succes(client_socket, aes_key, player, gamedata) :
    id_player, username, savePassword, x, y, money, sprout, fertilizer, fruits, arrosoir = player
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
        "gamedata" : gamedata,
        "players" : [{
            "username": u["username"],
            "x" : u["x"],
            "y" : u["y"],
            "move" : u["move"]
            } for u in connected.values()]
    })
    connected[client_socket] = {"username": username, "aes_key":aes_key, "x" : x, "y" : y, "move" : False}
    send_all_player({'type':'new_players', 'player':{'username':username, 'x':x, 'y':y}}, client_socket)  

@s.on("login")
def login(message, client_socket, aes_key) :

    if message["username"].strip() == "" or message["password"].strip() == "":
        message = {
            "type": "login",
            "response_type": "error",
            "message": "Username or password empty"
        }
        send(client_socket, aes_key, message)
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()

    else :

        username = message['username']
        password = message['password']

        if os.path.exists(os.sep.join([dataFolder, "json", "data_game.json"])) :
            gamedata = open(os.sep.join([dataFolder, "json", "data_game.json"]), 'r')
            gamedata = json.load(gamedata)
        else :
            gamedata = {}

        with engine.connect() as conn:
            player = conn.execute(text("SELECT * FROM players WHERE username = :username"), 
                         {"username":username}).fetchone()
        if player is not None :
            id_player, username, savePassword, x, y, money, sprout, fertilizer, fruits, arrosoir = player
            if bcrypt.checkpw(password.encode('utf-8'), savePassword.encode('utf-8')):
                login_succes(client_socket, aes_key, player, gamedata)
            else :
                send(client_socket, aes_key, {
                    "type": "login",
                    "response_type" : "error",
                    "message" : "Mauvais mot de passe"
                })
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()

        else :

            salt = bcrypt.gensalt()

            # Hacher le mot de passe
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')                    

            with engine.connect() as conn:
                result = conn.execute(text("insert into players (username, password) values (:username, :password)"), 
                         {"username":username, "password":hashed_password})
                conn.commit()
                id = result.lastrowid
                
            login_succes(
                client_socket,
                aes_key,
                (id, username, None, 0, 0, 0, 0, 0, 0, False),
                gamedata
            )

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
                    log.log(f"New message receive by {address[0]}:{address[1]}.")
                    if data["type"] == "init" :
                            compatible_version = ['1']
                            if data['version'] in compatible_version :

                                message = {
                                    "type": "init",
                                    "accept" : True,
                                    "public_key": base64.b64encode(encr.public_key).decode()
                                }

                                json_message = json.dumps(message) + "\n"
                                client_socket.sendall(json_message.encode('utf-8'))

                                aes_key = client_socket.recv(256)
                                aes_key = encr.private_key.decrypt(aes_key, encr.OAEP)

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
                chunk = encr.aes_decrypt(aes_key, iv, données_chiffrées).decode("utf-8")

                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    data = json.loads(line)
                    log.log(f"New message receive by {address[0]}:{address[1]}. " + ", ".join([f"{cle} : {value}" for cle, value in data.items()]) if data['type'] != 'login' else f"Type : {data["type"]}")
                    s.dispatch(data, client_socket, aes_key)
    except ConnectionResetError :
        pass
    try:
        client_socket.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    client_socket.close()

players = {}
server.settimeout(1.0)

try :
    while True:
        try :
            client_socket, address = server.accept()
        except socket.timeout:
            continue
        log.log(f"New connection of {address[0]}:{address[1]}")
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
