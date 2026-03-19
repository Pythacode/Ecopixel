# -------------------------------- Fruit ------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe fruits.                    #
# Crée par Lucas - https://github.com/GreGrenier/                        #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import pygame
from game import*


class Fruit():
    def __init__(self, x=0, y=0, type="apple"):
        
        self.size = (48, 48)

        self.apple = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "fruits.png"]))
        self.apple = pygame.transform.scale(self.apple, self.size)

        self.x = x
        self.y = y
        self.type = type

        self.actual_skin = self.apple

    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin, rect)

        x = main_game.player.x - offset_x
        if abs(self.x - 25 - x) < 100:
            main_game.tuto.next("recolte")
            main_game.player.fruits += 1
            main_game.game_view.fruits.remove(self)
