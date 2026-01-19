# -------------------------------- Game -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

from typing import Callable
import pygame

class view() :
    def __init__(self, init:Callable, update:Callable) -> None:
        """
        Crée une vue pour le jeux
        
        :param update: Une fonction qui sert à gérer actualiser la vue.. Elle doit attendre deux argument, la liste d'évènement et un objet surface qui correspond à l'écran.
        :type update: Callable
        :param init: Une fonction qui sert à initialiser la vue.
        :type init: Callable
        """
        self.init = init
        self.update = update


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


WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
