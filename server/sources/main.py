import socket
from colorama import *
import os
from datetime import datetime
import json
import threading

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

    def error(self, message) :
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        message = f"[{time}] [ERROR] : {message}\n"
        self.file.write(message)
        print(Fore.RED, message, Fore.RESET, sep="", end="")

    def log(self, message) :
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        message = f"[{time}] [INFO] : {message}\n"
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

    def dispatch(self, message, client_socket):
        handler = self.handlers.get(message["type"])
        if handler:
            handler(message, client_socket)

log = loggeur()
s = Serveur()

log.log(f'Script start')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try :
    config_file = open(os.sep.join([dataFolder, "json", "config.json"]))
    config = json.load(config_file)
except FileNotFoundError :
    log.error("Config file doesn't exsist. Use default config")
    config = {}

server.bind((config.get("HOST", "0.0.0.0"), config.get("IP", 2123)))
server.listen(5)

log.log(f'Serveur start on {server.getsockname()[0]}:{server.getsockname()[1]}')

@s.on("init")
def init_conn(message, client_socket) :
    compatible_version = ['1']
    if message['version'] in compatible_version :
        
        try :
            sauv_file = open(os.sep.join([dataFolder, "json", "data_game.json"]))
            sauv = json.load(sauv_file)
        except FileNotFoundError :
            log.error("Sauv file doesn't exsist. Use empty sauv")
            sauv = {}

        data_game_message = {
            "type": "data_game",
            "data" : sauv
        }
        data_game_message = json.dumps(data_game_message) + "\n"

        message = {
            "type": "init",
            "accept" : True,
            "data_game_lenght": len(data_game_message)
        }
    else :
        message = {
            "type": "init",
            "accept" : False
        }

    json_connexion_message = json.dumps(message) + "\n"
    client_socket.sendall(json_connexion_message.encode('utf-8'))

    client_socket.sendall(data_game_message.encode('utf-8'))

def handle_client(client_socket, address):
    buffer = ""
    try :
        while True:
            chunk = client_socket.recv(4096).decode('utf-8')
            if not chunk:
                break
            buffer += chunk
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                data = json.loads(line)
                log.log(f"New message receive by {address[0]}:{address[1]} : {data}")
                s.dispatch(data, client_socket)
    except ConnectionResetError :
        pass
    try:
        client_socket.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    client_socket.close()

players = []
server.settimeout(1.0)

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