# -------------------------------- Menu -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe maison.                    #
# Crée par Lucas - https://github.com/GreGrenier                         #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import pygame
import json
from game import*
from random import randint


class House():
    def __init__(self, x=0, y=0, lvl=1):
        
        self.size = (768, 768)

        self.house1 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "houses", "house1.png"]))
        self.house1 = pygame.transform.scale(self.house1, self.size)
        self.house2 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "houses", "house2.png"]))
        self.house2 = pygame.transform.scale(self.house2, self.size)
        self.house3 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "houses", "house3.png"]))
        self.house3 = pygame.transform.scale(self.house3, self.size)
        self.house4 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "houses", "house4.png"]))
        self.house4 = pygame.transform.scale(self.house4, self.size)

        self.x = x
        self.y = y
        self.lvl = lvl

        self.actual_skin = self.house1
        self.all_houses = [self.house1, self.house2, self.house3, self.house4]

    def change_skin(self):
        self.actual_skin = self.all_houses[self.lvl - 1]

    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin, rect)
