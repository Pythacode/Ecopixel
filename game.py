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

# Permet de crer main_game, dont menuView à besoin

from menu import menuView
main_game.change_view(menuView)

class button():

    def createButton(self, image_nor, image_mouse, image_click, screen, position, width, height, events):
        self.click = False
        image = pygame.image.load(image_nor)
        scaled_image = pygame.transform.scale(image, (width, height))
        rect = scaled_image.get_rect()
        rect.center = position
        if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            for event in events:
                if event == pygame.MOUSEBUTTONDOWN:
                    image = pygame.image.load(image_click)
                else:
                    image = pygame.image.load(image_mouse)
        scaled_image = pygame.transform.scale(image, (width, height))
        screen.blit(scaled_image, rect)
        return self.click
