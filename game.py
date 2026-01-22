# -------------------------------- Game -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
pygame.init()

class Game() :
    def __init__(self, WIDTH:int, HEIGHT:int):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.current_view = None
        self.WHITE = (255, 255, 255)
        self.BLACK = (000, 000, 000)
    
    def change_view(self, new_view) :
        self.screen.fill(self.BLACK)
        self.current_view = new_view
        self.current_view.init()

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
    
    # Create Button
    def createButton(self, screen):
        font = pygame.font.Font("freesansbold.ttf", 24)
        self.click = False
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
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        screen.blit(scaled_image, rect)
        screen.blit(rendertext, self.position)
        if self.click == True and self.OnClickFunc != None:
                self.OnClickFunc()


# INSEREZ LES CLASSES ET FONCTIONS ICI

# Permet de créer main_game, dont menuView à besoin
from menu import menuView
main_game.change_view(menuView)
