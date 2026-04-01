from datetime import datetime
from colorama import Fore
import os

class loggeur :
    def __init__(self, dataFolder):

        self.hour = None
        self.file = None
        self.dataFolder = dataFolder
        self.update_file()

    def update_file(self) :
        now = datetime.now()
        if self.hour != now.strftime("%H") :

            folder_path = now.strftime("logs/%Y/%m/%d")

            folder_path = self.asset_doc = os.sep.join([self.dataFolder, # Dossier data
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