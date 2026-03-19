# -------------------------------- Fruit ------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe cloud.                     #
# Crée par Lucas - https://github.com/GreGrenier/                        #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import pygame
from random import randint
from game import*


class Cloud():
    def __init__(self):
        
        self.size = (144, 144)

        self.cloud1 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "background", "cloud1.png"]))
        self.cloud1 = pygame.transform.scale(self.cloud1, self.size)
        self.cloud2 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "background", "cloud2.png"]))
        self.cloud2 = pygame.transform.scale(self.cloud2, self.size)
        self.cloud3 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "background", "cloud3.png"]))
        self.cloud3 = pygame.transform.scale(self.cloud3, self.size)

        self.x = randint(-100000, 100000)
        self.y = randint(450, 500)

        self.cloud_skin = [self.cloud1, self.cloud2, self.cloud3]
        self.actual_skin = self.cloud_skin[randint(0,2)]

    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x+offset_x/2, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin, rect)
