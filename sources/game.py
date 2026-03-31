# -------------------------------- Game -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par                                                               #
#          - Titouan - https://github.com/Pythacode/                     #
#          - Lucas - https://github.com/GreGrenier/                      #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import pygame
import os
import json
import sys
import socket
import queue
import threading
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

pygame.init()

OAEP = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)

class Game() :
    def __init__(self, WIDTH:int, HEIGHT:int):
        """
        A class for global variable
        """
        self.asset_doc = self.asset_doc = os.path.abspath(os.sep.join([os.path.split(__file__)[0], # Obtient le chemin absolus de `game.py`
                                                      '..', # Remonte d'un répertoir (Répertoir source)
                                                      'data' # Dossier data
                                                    ])) # Obligatoire pour gérer correctement l'execution depuis n'importe quel répertoire

        self.jsonPath = os.sep.join([self.asset_doc, 'json'])
        self.game_version = "1" # Version du jeu

        # Crée un écran pygame 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.current_view = None # Défini la vue actuelle à aucune (Les vues on besoin de main_game, impossible donc de les appelé sans avoir créé l'élément)
        
        self.running = True # Variable qui définie si la boucle principale (dans `main.py`) s'arrete ou non
        self.main_font_name = os.sep.join([self.asset_doc, "fonts", "return-of-the-boss.ttf"]) # Chemin de la police de base
        self.scroll_y = 0 # Valeur du scroll vertical
        self.scroll_x = 0 # Valeur du scroll horizontal
        self.touch_pressed = {} # Dictionnaire avec toutes les touches appuyées
        self.logo = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "logo.png"])) # Chemin du logo
        self.back = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "back.png"])) # Chemin de la flèche retour
        self.player = None # Variable joueur, idem que pour `current_view`
        self.house = None # Variable maison

        if os.path.exists(os.sep.join([self.jsonPath, "settings.json"])) :
            settings = open(os.sep.join([self.jsonPath, "settings.json"]), 'r')
            settings = json.load(settings)
        else :
            settings = {}
        
        self.key_move_right = settings.get('key_move_right', pygame.K_d) # Charge la clé `key_move_right` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche d
        self.key_move_left = settings.get('key_move_left', pygame.K_q) # Charge la clé `key_move_left` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche q
        self.key_action = settings.get('key_action', pygame.K_e) # Charge la clé `key_move_right` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche d
        self.key_pause = settings.get('key_pause', pygame.K_ESCAPE) # Charge la clé `key_pause` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche echape
        self.key_save = settings.get('key_sauv', pygame.K_o) # Charge la clé `key_sauv` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche o
        self.key_back = settings.get('key_back', pygame.K_ESCAPE) # Charge la clé `key_back` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche echape
        self.key_help = settings.get('key_help', pygame.K_h) # Charge la clé `key_help` du dictionnaire `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche h

        pygame.display.set_icon(self.logo) # Défini le logo de la fenêtre avec celui du jeux
        pygame.display.set_caption('Ecopixel') # Défini le titre de la fenêtre
        
        self.inbox = queue.Queue()   # messages reçus du serveur
        self.outbox = queue.Queue()  # messages à envoyer au serveur
        self.connect = False
        self.network_error = None

        self.views = {}

    def send_message(self, msg:dict) :
        message = json.dumps(msg) + "\n"
        self.client.send(message.encode('utf-8'))

    def change_view(self, new_view, args=tuple()) :
        """
        Docstring for change_view
        
        :param new_view: new view
        :param args: Arguments for view. Only first call of view.
        """
        
        if isinstance(new_view, type) :
            for attr, val in self.__dict__.items():
                if val is new_view:
                    new_view = new_view(*args)
                    setattr(self, attr, new_view)
                    break

        self.screen.fill('black')
        new_view.previous_view = self.current_view
        self.current_view = new_view
        self.scroll_y = 0
        self.scroll_x = 0
    
    def save(self) :
        """
        Sauvegarde les données du jeu
        Un texte "sauvegarde en cours" s'afficheras en bas à droite et l'écran vas freeze le temps de la sauvegarde
        """
        font = pygame.font.Font(self.main_font_name, 24) # Charge la police
        w, h = font.size('Sauvegarde en cours...') # Obtient la taille du texte
        word_surface = font.render('Sauvegarde en cours...', 0, 'black') # Crée un élément affichable a partir du texte
        ws, hs = self.screen.get_size() # Obtient la taille de l'écran
        self.screen.blit(word_surface, (ws - w - 5, hs - h - 5)) # Affiche le texte en bas à droite
        pygame.display.flip() # Actualise l'affichage
        
        if not isinstance(main_game.game_view, type) : # On lance la sauvegarde si la vue du jeux à été ouverte

            # Crée un dictionnaire avec les données à sauvegarder
            sauv = {
                    'player' : 
                        {
                            'x' : self.player.x + self.game_view.offset_x,
                            'y' : self.player.y,
                            'money' : self.player.money,
                            'sprout' : self.player.sprout,
                            'fertilizer' : self.player.fertilizer,
                            'orientation' : self.player.orientation,
                            'skin_index' : self.player.skin_index,
                            'plant' : self.player.plant,
                            'fruits': self.player.fruits,
                            'arrosoir': self.player.arrosoir,
                            'tuto_advancement' : self.tuto.advencement
                        },
                    'game' :
                        {
                            'wait_tree' : None if self.game_view.wait_tree == None else {
                                'x' : self.game_view.wait_tree.get('x'),
                                'y' : self.game_view.wait_tree.get('y'),
                                'type': self.game_view.wait_tree.get('type'),
                                'fertilized': self.game_view.wait_tree.get('fertilized')
                                },
                            'trees' : [
                                    {
                                        'x' : t.x,
                                        'y' : t.y,
                                        'time_alive' : t.time_alive,
                                        'type' : t.type,
                                        'seedling': t.seedling,
                                        'growned_up': t.growned_up,
                                        'skin_index': t.skin_index,
                                        'max_alive': t.max_alive,
                                        'fertilized': t.fertilized
                                    } for t in self.game_view.trees
                                ],
                            'house':{
                                'lvl': self.game_view.h.lvl
                                }
                        }
                }

            with open(os.sep.join([self.jsonPath, 'sauv_game.json']), 'w', encoding='utf-8') as f: # Ouvre le fichier de sauvegarde
                json.dump(sauv, f, ensure_ascii=False, indent=4) # Enrigistrer les données sous forme de JSON
        

        if not isinstance(main_game.settings_view, type) : # On lance la sauvegarde si la vue du jeux à été ouverte

            settings = {
                        'key_move_right' : self.key_move_right,
                        'key_move_left' : self.key_move_left,
                        'key_action' : self.key_action,
                        'key_pause' : self.key_pause,
                        'key_sauv' : self.key_save,
                        'key_back' : self.key_back,
                    }
            
            with open(os.sep.join([self.jsonPath, 'settings.json']), 'w', encoding='utf-8') as f: # Ouvre le fichier de sauvegarde
                json.dump(settings, f, ensure_ascii=False, indent=4) # Enrigistrer les données sous forme de JSON
     

    def aes_encrypt(self, aes_key, message: bytes) -> bytes:
        iv = os.urandom(16)
        # Padding PKCS7
        pad = 16 - len(message) % 16
        pad_message = message + bytes([pad] * pad)
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        encrypter = cipher.encryptor()
        encrypt_data = encrypter.update(pad_message) + encrypter.finalize()
        return iv + encrypt_data

    def aes_decrypt(self, aes_key, iv, data):
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        decrypteur = cipher.decryptor()
        données = decrypteur.update(data) + decrypteur.finalize()
        pad = données[-1]
        return données[:-pad]

    def network_thread(self, port, hostname):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try :
            client.connect((hostname, port))  
            self.connect = True
        except ConnectionRefusedError :
            self.network_error = "Aucune connexion n'a pu être établie car l'ordinateur cible l'a expressément refusée"
            return

        
        message = {
            "type" : 'init',
            'version' : self.game_version
        }
        
        message = json.dumps(message) + "\n"
        client.sendall(message.encode('utf-8'))

        data = json.loads(client.recv(700))

        if not data['accept'] :
            print("Connexion impossible\nLa version de votre client n'est pas compatible avec le serveur.")
            pygame.quit()
            sys.exit()

        public_key_pem = base64.b64decode(data["public_key"])
        public_key = serialization.load_pem_public_key(public_key_pem)

        aes_key = os.urandom(32)  # AES-256
        aes_key_crypted = public_key.encrypt(aes_key, OAEP)
        client.sendall(aes_key_crypted)        

        # Thread d'envoi
        def send_loop():
            while True:
                data = self.outbox.get()  # attend qu'un message soit à envoyer
                message = json.dumps(data) + "\n"
                paquet = self.aes_encrypt(aes_key, message.encode())
                client.sendall(len(paquet).to_bytes(4, "big") + paquet)

        threading.Thread(target=send_loop, daemon=True).start()

        # Réception dans ce thread
        buffer = ""
        while True:
            entête = client.recv(4)
            if not entête:
                break
            taille = int.from_bytes(entête, "big")
            paquet = client.recv(taille)
            iv = paquet[:16]
            données_chiffrées = paquet[16:]
            chunk = self.aes_decrypt(aes_key, iv, données_chiffrées).decode("utf-8")
            buffer += chunk
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                self.inbox.put(json.loads(line))
            
class button():

    def __init__(self, image_nor, image_mouse, image_click, position, width, height, OnClickFunc, text=""):
        """
        Initialise les paramètres d'un bouton
        
        :param image_nor: Chemin de l'image normale dans les fichier sous la forme "os.sep.join([])"
        :param image_mouse: Chemin de l'image hover dans les fichier sous la forme "os.sep.join([])"
        :param image_click: Chemin de l'image cliqué dans les fichier sous la forme "os.sep.join([])"
        :param position: Position sous forme de tuple (x,y)
        :param width: Largeur du bouton en int
        :param height: Hauteur de bouton en int
        :param OnClickFunc: Fonction executé quand le bouton est cliqué
        :param text: (Optionnel) Texte à afficher sur le bouton en str
        """
        self.image_nor = pygame.image.load(image_nor)
        self.image_mouse = pygame.image.load(image_mouse)
        self.image_click = pygame.image.load(image_click)
        self.width = width
        self.height = height
        self.OnClickFunc = OnClickFunc
        self.text = text
        self.position = position
        self.click = False
        font = pygame.font.Font(main_game.main_font_name, 24)
        image = self.image_nor
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = scaled_image.get_rect()
        self.rendertext = font.render(self.text, True, 'black')

    def update(self, screen, position=""):
        if position == "" : position = self.position
        buttonpos = (position[0] - self.rendertext.get_size()[0]/2, position[1] - self.rendertext.get_size()[1]/2)
        self.rect.center = position
        image = self.image_nor
        if self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                image = self.image_click
                self.click = True
            else:
                image = self.image_mouse
                self.click = False
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        screen.blit(scaled_image, self.rect)
        screen.blit(self.rendertext, buttonpos)
        if self.click == True and self.OnClickFunc != None:
                self.OnClickFunc()
                self.click = False
        screen.blit(scaled_image, self.rect)
        screen.blit(self.rendertext, buttonpos)

class entry_text() :
    def __init__(self, surface:pygame.surface, color, pos:tuple, size:tuple, width:int, border_radius:int, font:pygame.font, backround_color=(0, 0, 0, 0), replace=None):
        """
        A entry text
        
        :param surface: Screen where entry text as display
        :type surface: pygame.surface
        :param color: Color of entry text
        :type color: pygame.Color | tuple
        :param pos: Position of entry text
        :type pos: tuple
        :param size: Size of entry
        :type size: tuple
        :param width: Width de la zone
        :type width: int
        :param border_radius: Border radius
        :type border_radius: int
        :param font: font of text.
        :type font: pygame.font
        """
        self.active = False
        self.text = []
        self.font = font
        self.x, self.y = pos
        self.color = color
        self.surface = surface
        self.width = width
        self.border_radius = border_radius
        self.search_zone = pygame.Rect(pos, size)
        self.last_change = 0
        self.cursor = True
        self.cursor_index = 0
        self.backround_color = backround_color
        self.replace=replace

    def get_text(self) -> str :
        """
        Return text in input
        """

        return ''.join(self.text)
    
    def update(self, events:list, pos=None, size=None) :
        """
        Update function
        
        :param events: List of pygame evenements
        :type events: list
        """
        if pos :
            x, y = pos
            self.search_zone[0:2] = pos
        else :
            x, y = self.x, self.y

        if size :
            self.search_zone[2:4] = size

        return_value = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.search_zone.collidepoint(event.pos):
                    self.active = True
                else :
                    self.active = False
            if self.active :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN:
                        self.active = False
                        return_value = ''.join(self.text)
                    elif event.key == pygame.K_BACKSPACE:
                        if self.cursor_index != 0 :
                            del self.text[self.cursor_index-1]
                            self.cursor_index -=1
                    elif event.key == pygame.K_DELETE :
                        if self.cursor_index != len(self.text) :
                            del self.text[self.cursor_index]
                    elif event.key == pygame.K_LEFT:
                        if self.cursor_index > 0 :
                            self.cursor_index -=1
                    elif event.key == pygame.K_RIGHT:
                        if self.cursor_index < len(self.text) :
                            self.cursor_index +=1
                if event.type == pygame.TEXTINPUT :
                    self.text.insert(self.cursor_index, event.text)
                    self.cursor_index +=1

        if self.active :
            now = pygame.time.get_ticks()
            if now - self.last_change > 500 :
                self.cursor = not self.cursor
                self.last_change = now
            
        text = ''.join(self.text)
        
        if self.replace :
            text = self.replace * len(text)

        pygame.draw.rect(self.surface, self.backround_color, self.search_zone, border_radius=self.border_radius)
        pygame.draw.rect(self.surface, self.color, self.search_zone, self.width, border_radius=self.border_radius)
        search_text = self.font.render(text, True, 'black')
        self.surface.blit(search_text, (x+10, y+5))
        if self.cursor and self.active :
            cursor = self.font.render("|", True, 'black')
            self.surface.blit(cursor, (x + 10 + self.font.size(text[:self.cursor_index])[0] - (self.font.size("|")[0]/4), y+5))

def draw_header() :
    width = main_game.screen.get_size()[0]
    pygame.draw.rect(main_game.screen, (166, 85, 78), (0, 0, width, 40))
    font = pygame.font.Font(main_game.main_font_name, 24)

    # Logo
    scaled_logo = pygame.transform.scale(main_game.logo, (35, 35))
    main_game.screen.blit(scaled_logo, (2.5, 2.5))

    data = (
        (os.sep.join([main_game.asset_doc, "image", "icon", "coin.png"]), str(main_game.player.money)), # Coin
        (os.sep.join([main_game.asset_doc, "image", "icon", "sprout.png"]), str(main_game.player.sprout)), # Sprout
        (os.sep.join([main_game.asset_doc, "image", "item", "fertilizer.png"]), str(main_game.player.fertilizer)), # Fertilizer
        (os.sep.join([main_game.asset_doc, "image", "icon", "fruits.png"]), str(main_game.player.fruits)), # Fruits
    )

    start_pos = 20
    gap = 40

    for image, label in data :

        w = font.size(label)[0] + gap
        start_pos += w

        pygame.draw.rect(main_game.screen, (131, 50, 43), (width - start_pos, 5, w, 30), border_radius=20)

        image = pygame.image.load(image)
        scaled_image = pygame.transform.scale(image, (30, 30))
        main_game.screen.blit(scaled_image, (width - start_pos - 5, 5))

        coin_count = font.render(label, True, 'white')
        main_game.screen.blit(coin_count, (width - start_pos + 30, 3))

        start_pos += 20 # Gap betwen count

        image_arrosoir,rect_arrosoir = img(45,30, (width - start_pos - 20, 20),"item","arrosoir.png")
    if main_game.player.arrosoir == True :
        main_game.screen.blit(image_arrosoir,rect_arrosoir)



        
    """

    pygame.draw.rect(main_game.screen, (131, 50, 43), (width - start_pos, 5, w, 30), border_radius=20)

    coin_image = pygame.image.load()
    scaled_coin = pygame.transform.scale(coin_image, (30, 30))
    main_game.screen.blit(scaled_coin, (width - start_pos - 10, 5))

    coin_count = font.render(, True, 'white')
    main_game.screen.blit(coin_count, (width - start_pos + 30, 3))"""


def size_text(text:str, font:pygame.font, max_width:int) -> int:
        """
        Calcuate size of a text
        Original code : https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame

        :param text: Text to draw
        :type text: str
        :param font: Font to draw text
        :type font: pygame.font
        :param max_width: Width we cant exceed
        :type max_width: int
        :return: The height of text
        :rtype: int
        """
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        x, y = 0, 0
        count_line = 1
        m_width = 0
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, 'white')
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = 0  # Reset the x.
                    y += word_height  # Start on new row.
                else :                    
                    if x + word_width > m_width :
                        m_width = x + word_width
                x += word_width + space
            x = 0  # Reset the x.
            y += word_height  # Start on new row.
            count_line += 1
        return y, m_width

def blit_text(text:str, pos:tuple, font:pygame.font, max_width:int, color, screen:pygame.surface) -> int:
        """
        Draw `text` on `screen` with lines-split for not exceed `max_width`
        Original code : https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame

        :param text: Text to draw
        :type text: str
        :param pos: A tuple with position `(x, y)`
        :type pos: tuple
        :param font: Font to draw text
        :type font: pygame.font
        :param max_width: Width we cant exceed
        :type max_width: int
        :param color: Color of text
        :type color:pygame.Color | tuple
        :param screen: Screen where text as display
        :type screen: pygame.surface
        :return: The height of text
        :rtype: int
        """
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        x, y = pos
        count_line = 1
        word_height = 0 # Si `text` est vide, revoie pas d'erreur
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= pos[0] + max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            count_line += 1

        return count_line * word_height

def img(width,height,position,dossier,png):
    """
    Données pour la fonction img:
    :param width: Largeur de l'image en int
    :param height: Hauteur de l'image en int
    :param x: Position horizontale de l'image en int
    :param y: Position verticale de l'image en int
    :param path: Chemin dans les fichier de l'image à afficher en str
    """
        # Résultat : Affiche une image sur la fenêtre

    image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", dossier, png]))
    image = pygame.transform.scale(image, (width,height))
    rect = image.get_rect()
    rect.center = position
    return image, rect

# INSEREZ LES CLASSES ET FONCTIONS ICI

main_game = Game(
    WIDTH=1280,
    HEIGHT=720
) # Garder ici avant l'import, sinon main_game ne sera pas defini
# Permet de créer main_game, dont menuView à besoin

from views.menu import menuView
from views.gameView import gameView
from views.searchEngine import searchView
from views.shop import shopView
from views.setting import settingView
from views.server import serverView
from sprites.player import Player

main_game.menu_view = menuView
main_game.game_view = gameView
main_game.search_view = searchView
main_game.shop_view = shopView
main_game.settings_view = settingView
main_game.server_view = serverView

main_game.change_view(main_game.menu_view)