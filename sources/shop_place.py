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


class Shop_place():
    def __init__(self, x=250, y=-10):
        
        self.image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "shop", "shop.png"]))

        imageJsonFile = open(os.sep.join([main_game.asset_doc, "image", "shop", "shop_frame.json"]), 'r')
        self.tilesetjson = json.load(imageJsonFile)

        self.size = (400, 400)

        # Shop's Frames
        self.shopright = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Shop Right"]["frame"]["x"],
                        self.tilesetjson["Shop Right"]["frame"]["y"],
                        self.tilesetjson["Shop Right"]["frame"]["w"],
                        self.tilesetjson["Shop Right"]["frame"]["h"]
                    )
        }
        self.shopright["subsurface"] = pygame.transform.scale(self.shopright["subsurface"], self.size)
        self.shopleft= {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Shop Left"]["frame"]["x"],
                        self.tilesetjson["Shop Left"]["frame"]["y"],
                        self.tilesetjson["Shop Left"]["frame"]["w"],
                        self.tilesetjson["Shop Left"]["frame"]["h"]
                    )
        }
        self.shopleft["subsurface"] = pygame.transform.scale(self.shopleft["subsurface"], self.size)

        self.x = x
        self.y = y

        self.actual_skin = self.shopright
        self.shops_frame = [self.shopright, self.shopleft]

    def change_skin(self, offset_x):
        x = main_game.player.x - offset_x
        if x - 150 < self.x:
            self.actual_skin = self.shopleft
        else:
            self.actual_skin = self.shopright

    def draw(self, surface, ground_altitude, offset_x) :
        self.change_skin(offset_x)
        rect = self.actual_skin["subsurface"].get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin["subsurface"], rect)
