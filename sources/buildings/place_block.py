# -------------------------------- Menu -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe decoration.                #
# Crée par Lucas - https://github.com/GreGrenier/                        #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #
import os
import pygame
import json
from game import*

class Decoration():
    def __init__(self, offset_x, type=""):

        self.blocks = {
            "test": {"dir":[main_game.asset_doc, "image", "button", "button_nor.png"], "size":(32,32)}
        }

        self.x = 0
        self.y = 0
        self.placing(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], offset_x, type)
    
    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin, rect)
        

    def placing(self, x:int, y:int, offset_x, type=""):
        self.x = x + offset_x
        self.y = abs(y - main_game.screen.get_size()[1])
        self.actual_skin = pygame.image.load(os.sep.join(self.blocks[type]["dir"]))
        self.actual_skin = pygame.transform.scale(self.actual_skin, self.blocks[type]["size"])
        self.size = self.blocks[type]["size"]
        print(self.x)
        print(self.y)

