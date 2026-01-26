# -------------------------------- Game -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
import os
pygame.init()

class Game() :
    def __init__(self, WIDTH:int, HEIGHT:int):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.current_view = None
        self.WHITE = (255, 255, 255)
        self.BLACK = (000, 000, 000)
        self.running = True
        self.asset_doc = "assets"
        self.main_font_name = "freesansbold.ttf"
        self.scroll_y = 0
        self.scroll_x = 0

    def blit_text(self, text:str, pos:tuple, font:pygame.font, max_width, color) -> int:
        """
        Draw `text` on `self.screen` with lines-split for not exceed `max_width`
        Original code : https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame

        :param text: Text to draw
        :type text: str
        :param pos: A tuple with position `(x, y)`
        :type tuple: int
        :param font: Font to draw text
        :type font: pygame.font
        :param max_width: Width we cant exceed
        :type max_width: int
        :param color: Color of text
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
                self.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            count_line += 1

        return count_line * word_height
    
    def change_view(self, new_view) :
        self.screen.fill(self.BLACK)
        self.current_view = new_view()
        self.scroll_y = 0
        self.scroll_x = 0

main_game = Game(
    WIDTH=1280,
    HEIGHT=720
)

class button():

    def __init__(self, image_nor, image_mouse, image_click, position, width, height, OnClickFunc, text=""):
        self.image_nor = image_nor
        self.image_mouse = image_mouse
        self.image_click = image_click
        self.position = position
        self.width = width
        self.height = height
        self.OnClickFunc = OnClickFunc
        self.text = text
        self.click = False
    
    # Create Button
    def createButton(self, screen):
        font = pygame.font.Font("freesansbold.ttf", 24)
        image = pygame.image.load(self.image_nor)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        rect = scaled_image.get_rect()
        rect.center = self.position
        rendertext = font.render(self.text, True, main_game.BLACK)
        if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                image = pygame.image.load(self.image_click)
                self.click = True
            else:
                image = pygame.image.load(self.image_mouse)
                self.click = False
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        screen.blit(scaled_image, rect)
        screen.blit(rendertext, self.position)
        if self.click == True and self.OnClickFunc != None:
                self.OnClickFunc()

class entry_text() :
    def __init__(self, surface, color, pos, size, width, border_radius, font):
        self.active = False
        self.text = []
        self.font = font
        self.x, self.y = pos
        self.color = color
        self.surface = surface
        self.width = width
        self.border_radius = border_radius
        self.search_zone = pygame.Rect(pos, (size))
        self.last_change = 0
        self.cursor = True
        self.cursor_index = 0
    
    def update(self, events) :
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
            #text.insert(self.cursor_index, self.cursor)
            text = ''.join(text)

        else :
            text = ''.join(self.text)
        
        pygame.draw.rect(self.surface, self.color, self.search_zone, self.width, border_radius=self.border_radius)
        search_text = self.font.render(text, True, main_game.BLACK)
        self.surface.blit(search_text, (self.x+10, self.y+7))
        if self.cursor :
            cursor = self.font.render("|", True, main_game.BLACK)
            self.surface.blit(cursor, (self.x + 10 +self.font.size(text[:self.cursor_index])[0] - (self.font.size("|")[0]/4), self.y+7))

        return return_value

# INSEREZ LES CLASSES ET FONCTIONS ICI

# Permet de créer main_game, dont menuView à besoin
from menu import menuView
main_game.change_view(menuView)
