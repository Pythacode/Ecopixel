# -------------------------------- Game -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
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
        self.asset_doc = "data"

        if os.path.exists(os.sep.join([self.asset_doc, "data_game.json"])) :
            dataJsonfile = open(os.sep.join([self.asset_doc, "data_game.json"]), 'r')
            self.data = json.load(dataJsonfile)
        else :
            self.data = {}

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.current_view = None
        self.WHITE = (255, 255, 255)
        self.BLACK = (000, 000, 000)
        self.running = True
        self.main_font_name = os.sep.join([self.asset_doc, "fonts", "return-of-the-boss.ttf"]) #"freesansbold.ttf"
        self.scroll_y = 0
        self.scroll_x = 0
        self.touch_pressed = {}
        self.logo = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "logo.png"]))
        self.back = pygame.image.load(os.sep.join([self.asset_doc, "image", "icon", "back.png"]))
        self.player = None
        
        settings_data = self.data.get('settings', {})
        self.key_move_right = settings_data.get('key_move_right', pygame.K_d)
        self.key_move_left = settings_data.get('key_move_left', pygame.K_q)
        self.key_plant = settings_data.get('key_plant', pygame.K_e)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('Ecopixel')
    
    def change_view(self, new_view) :
        """
        Docstring for change_view
        
        :param new_view: new view
        """
        self.screen.fill(self.BLACK)
        new_view.previous_view = self.current_view
        self.current_view = new_view
        self.scroll_y = 0
        self.scroll_x = 0

main_game = Game(
    WIDTH=1280,
    HEIGHT=720
)

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
                if x + word_width >= max_width:
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
        self.image_nor = pygame.image.load(image_nor)
        self.image_mouse = pygame.image.load(image_mouse)
        self.image_click = pygame.image.load(image_click)
        self.position = position
        self.width = width
        self.height = height
        self.OnClickFunc = OnClickFunc
        self.text = text
        self.click = False

    def update(self, screen):
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
        screen.blit(self.rendertext, self.position)
        if self.click == True and self.OnClickFunc != None:
                self.OnClickFunc()
                self.click = False
        screen.blit(scaled_image, self.rect)
        screen.blit(self.rendertext, self.position)

    # Create Button
    def createButton(self):
        font = pygame.font.Font("freesansbold.ttf", 24)
        image = self.image_nor
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = scaled_image.get_rect()
        self.rect.center = self.position
        self.rendertext = font.render(self.text, True, main_game.BLACK)
        

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
        self.previous_view = None
    
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
        search_text = self.font.render(text, True, main_game.BLACK)
        self.surface.blit(search_text, (self.x+10, self.y+5))
        if self.cursor and self.active :
            cursor = self.font.render("|", True, main_game.BLACK)
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

    coin_count = font.render(str(main_game.player.money), True, main_game.WHITE)
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

    coin_count = font.render(str(main_game.player.sprout), True, main_game.WHITE)
    main_game.screen.blit(coin_count, (width - start_pos + 30, 3))


# INSEREZ LES CLASSES ET FONCTIONS ICI

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
