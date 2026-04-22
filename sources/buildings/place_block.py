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
    def __init__(self, offset_x, ground_height, type=""):

        self.blocks = {
            "test": {"dir":[main_game.asset_doc, "image", "game", "ground.png"], "size":(32,32)}
        }

        self.x = 0
        self.y = 0 # pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]#
        self.placing(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], offset_x, ground_height, type)
    
    def draw(self, surface, ground_altitude, offset_x) :
        #self.placing(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], offset_x, "test")
        rect = self.actual_skin.get_rect()
        rect.center = self.x+offset_x, ground_altitude - self.y - 32
        surface.blit(self.actual_skin, rect)

    def placing(self, x:int, y:int, offset_x, ground_height, type=""):
        self.x = x - offset_x
        self.y = (main_game.screen.get_size()[1] - pygame.mouse.get_pos()[1] - ground_height) - self.blocks[type]["size"][1]
        self.actual_skin = pygame.image.load(os.sep.join(self.blocks[type]["dir"]))
        self.actual_skin = pygame.transform.scale(self.actual_skin, self.blocks[type]["size"])
        self.size = self.blocks[type]["size"]
        print(self.x, x, offset_x, self.x+offset_x)
        print(self.y, y)

