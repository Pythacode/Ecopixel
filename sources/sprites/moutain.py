# -------------------------------- Fruit ------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe mountain.                     #
# Crée par Lucas - https://github.com/GreGrenier/                        #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import pygame
from random import randint
from game import*


class Mountain():
    def __init__(self):
        
        self.size = (448, 128)

        self.mountain = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "background", "mountains.png"]))
        self.mountain = pygame.transform.scale(self.mountain, self.size)

        self.x = randint(-100000, 100000)
        self.y = 0

        self.actual_skin = self.mountain

    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x+offset_x/3, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin, rect)
