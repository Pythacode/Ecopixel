# -------------------------------- Game -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import pygame
import os
import json

pygame.init()

class Game() :
    def __init__(self, WIDTH:int, HEIGHT:int):
        """
        A class for global variable
        """
        self.asset_doc = self.asset_doc = os.path.abspath(os.sep.join([os.path.split(__file__)[0], # Obtient le chemin absolus de `game.py`
                                                      '..', # Remonte d'un répertoir (Répertoir source)
                                                      'data' # Dossier data
                                                    ])) # Obligatoir pour correctement gerer l'execution depuis n'importe quel répertoire

        if os.path.exists(os.sep.join([self.asset_doc, "data_game.json"])) : # Si une sauvegarde exsiste
            dataJsonfile = open(os.sep.join([self.asset_doc, "data_game.json"]), 'r') # On ouvre le fichier
            self.data = json.load(dataJsonfile) # On charge la sauvegarde dans le dictionnair `self.data`
        else :
            self.data = {} # Sinon on enregistre un dictionnair vide pour `self.data`

        # Crée un écran pygame 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.current_view = None # Défini la vue actuelle à aucune (Les vues on besoin de main_game, impossible donc de les apellé sans avoir créé l'élément)
        
        self.running = True # Variable qui définie si la boucle principal (dans `main.py` s'arette ou non)
        self.main_font_name = os.sep.join([self.asset_doc, "fonts", "return-of-the-boss.ttf"]) # Chemin de la police de base
        self.scroll_y = 0 # Valeur du scroll vertical
        self.scroll_x = 0 # Valeur du scroll horizontal
        self.touch_pressed = {} # Dictionnaire avec toute les touche appuyé
        self.logo = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "logo.png"])) # Chemin du logo
        self.back = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "back.png"])) # Chemin de la fleche retour
        self.player = None # Variable joueur, idem que pour `current_view`
        
        settings_data = self.data.get('settings', {}) # Charge la valeur de la clé `settings` du dictionnair `self.data` dans settings_data. Si la clé `settings` n'exsiste pas, on enregistre un dictionnair vide
        self.key_move_right = settings_data.get('key_move_right', pygame.K_d) # Charge la clé `key_move_right` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche d
        self.key_move_left = settings_data.get('key_move_left', pygame.K_q) # Charge la clé `key_move_left` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche q
        self.key_plant = settings_data.get('key_plant', pygame.K_e) # Charge la clé `key_move_right` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche d
        self.key_pause = settings_data.get('key_pause', pygame.K_ESCAPE) # Charge la clé `key_pause` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche echape
        self.key_save = settings_data.get('key_sauv', pygame.K_o) # Charge la clé `key_sauv` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche o
        self.key_back = settings_data.get('key_back', pygame.K_o) # Charge la clé `key_back` du dictionnair `settings_data`. Si elle n'exsiste pas, on charge la valeur par default : le code de la touche echape

        pygame.display.set_icon(self.logo) # Défini le logo de la fenetre avec celui du jeux
        pygame.display.set_caption('Ecopixel') # Défini le titre de la fenetre
    
    def change_view(self, new_view) :
        """
        Docstring for change_view
        
        :param new_view: new view
        """
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
        font = font = pygame.font.Font(self.main_font_name, 24) # Charge la police
        w, h = font.size('Sauvegarde en cours...') # Optien la taille du texte
        word_surface = font.render('Sauvegarde en cours...', 0, 'black') # Crée un élément affichable a partir du texte
        ws, hs = self.screen.get_size() # Obtient la taille de l'écran
        self.screen.blit(word_surface, (ws - w - 5, hs - h - 5)) # Affiche le texte en bas à droite
        pygame.display.flip() # Actualise l'affichage
        house = self.game_view.h

        # Crée un dictionnaire avec les données à sauvegarder
        data = {
                'player' : 
                    {
                        'x' : self.player.x,
                        'y' : self.player.y,
                        'money' : self.player.money,
                        'sprout' : self.player.sprout,
                        'orientation' : self.player.orientation,
                        'skin_index' : self.player.skin_index,
                        'plant' : self.player.plant
                    },
                'settings' :
                    {
                        'key_move_right' : self.key_move_right,
                        'key_move_left' : self.key_move_left,
                        'key_plant' : self.key_plant,
                        'key_pause' : self.key_pause,
                        'key_sauv' : self.key_save,
                    },
                'game' :
                    {
                        'wait_tree' : None if self.game_view.wait_tree == None else {
                            'x' : self.game_view.wait_tree.get('x'),
                            'y' : self.game_view.wait_tree.get('y'),
                            'type': self.game_view.wait_tree.get('type')
                            },
                        'trees' : [{
                            'x' : t.x,
                            'y' : t.y,
                            'time_alive' : t.time_alive,
                            'type' : t.type,
                            'seedling': t.seedling,
                            'growned_up': t.growned_up,
                            'skin_index': t.skin_index,
                            'max_alive': t.max_alive
                            } for t in self.game_view.trees],
                        'house':{
                            'lvl': house.lvl
                        }
                    }
            }

        with open(os.sep.join([self.asset_doc, 'data_game.json']), 'w', encoding='utf-8') as f: # Ouvre le fichier de sauvegarde
            json.dump(data, f, ensure_ascii=False, indent=4) # Enrigistrer les données sous forme de JSON
            

def size_text(text:str, font:pygame.font, max_width:int, color:pygame.Color | tuple, screen:pygame.surface) -> int:
        """
        Calcuate size of a text
        Original code : https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame

        :param text: Text to draw
        :type text: str
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
        x, y = 0, 0
        count_line = 1
        m_width = 0
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width > m_width :
                    m_width = x + word_width
                if x + word_width >= max_width:
                    if x + word_width > m_width :
                        m_width = x + word_width
                    x = 0  # Reset the x.
                    y += word_height  # Start on new row.
                x += word_width + space
            x = 0  # Reset the x.
            y += word_height  # Start on new row.
            count_line += 1

        return count_line * word_height, m_width

def blit_text(text:str, pos:tuple, font:pygame.font, max_width:int, color:pygame.Color | tuple, screen:pygame.surface) -> int:
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
        screen.blit(self.rendertext, position)
        if self.click == True and self.OnClickFunc != None:
                self.OnClickFunc()
                self.click = False
        screen.blit(scaled_image, self.rect)
        screen.blit(self.rendertext, position)
        

class entry_text() :
    def __init__(self, surface:pygame.surface, color:pygame.Color | tuple, pos:tuple, size:tuple, width:int, border_radius:int, font:pygame.font):
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
    
    def update(self, events:list) :
        """
        Update function
        
        :param events: List of pygame evenements
        :type events: list
        """
        return_value = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.search_zone.collidepoint(event.pos):
                    self.active = True
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
                    else:
                        if event.unicode != "" :
                            self.text.insert(self.cursor_index, event.unicode)
                            self.cursor_index +=1

        if self.active :
            now = pygame.time.get_ticks()
            if now - self.last_change > 500 :
                self.cursor = not self.cursor
                self.last_change = now
            
            text = self.text[:]
            text = ''.join(text)

        else :
            text = ''.join(self.text)
        
        pygame.draw.rect(self.surface, self.color, self.search_zone, self.width, border_radius=self.border_radius)
        search_text = self.font.render(text, True, 'black')
        self.surface.blit(search_text, (self.x+10, self.y+5))
        if self.cursor and self.active :
            cursor = self.font.render("|", True, 'black')
            self.surface.blit(cursor, (self.x + 10 + self.font.size(text[:self.cursor_index])[0] - (self.font.size("|")[0]/4), self.y+5))

        return return_value

def draw_header() :
    width = main_game.screen.get_size()[0]
    pygame.draw.rect(main_game.screen, (166, 85, 78), (0, 0, width, 40))
    font = pygame.font.Font(main_game.main_font_name, 24)

    # Logo
    scaled_logo = pygame.transform.scale(main_game.logo, (35, 35))
    main_game.screen.blit(scaled_logo, (2.5, 2.5))

    # Coin
    gap = 84 + font.size(str(main_game.player.money))[0]
    if gap > 300 : gap = 100
    start_pos = gap if gap > 100 else 100
    w = gap-40

    pygame.draw.rect(main_game.screen, (131, 50, 43), (width - start_pos, 5, w, 30), border_radius=20)

    coin_image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "coin.png"]))
    scaled_coin = pygame.transform.scale(coin_image, (30, 30))
    main_game.screen.blit(scaled_coin, (width - start_pos - 10, 5))

    coin_count = font.render(str(main_game.player.money), True, 'white')
    main_game.screen.blit(coin_count, (width - start_pos + 30, 3))

    # Sprout
    gap = 84 + font.size(str(main_game.player.sprout))[0]
    if gap > 300 : gap = 100
    start_pos += gap if gap > 100 else 100
    w = gap-40

    pygame.draw.rect(main_game.screen, (131, 50, 43), (width - start_pos, 5, w, 30), border_radius=20)

    coin_image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "sprout.png"]))
    scaled_coin = pygame.transform.scale(coin_image, (30, 30))
    main_game.screen.blit(scaled_coin, (width - start_pos - 10, 5))

    coin_count = font.render(str(main_game.player.sprout), True, 'white')
    main_game.screen.blit(coin_count, (width - start_pos + 30, 3))


# INSEREZ LES CLASSES ET FONCTIONS ICI

main_game = Game(
    WIDTH=1280,
    HEIGHT=720
) # Garder ici avant l'import, sinon main_game ne seras pas defini

# Permet de créer main_game, dont menuView à besoin
from menu import menuView
from gameView import gameView
from searchEngine import searchView
from shop import shopView
from player import Player
from setting import settingView

main_game.menu_view = menuView()
main_game.game_view = gameView()
main_game.search_view = searchView()
main_game.shop_view = shopView()
main_game.settings_view = settingView()

main_game.change_view(main_game.menu_view)
main_game.player = Player(main_game.screen.get_size()[0] / 2)
