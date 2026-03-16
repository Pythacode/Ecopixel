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
        # Shop Right
        self.right0 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Right 0"]["frame"]["x"],
                        self.tilesetjson["Right 0"]["frame"]["y"],
                        self.tilesetjson["Right 0"]["frame"]["w"],
                        self.tilesetjson["Right 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Right 0"]["duration"]
        }
        self.right0["subsurface"] = pygame.transform.scale(self.right0["subsurface"], self.size)
        self.right1 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Right 1"]["frame"]["x"],
                        self.tilesetjson["Right 1"]["frame"]["y"],
                        self.tilesetjson["Right 1"]["frame"]["w"],
                        self.tilesetjson["Right 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Right 1"]["duration"]
        }
        self.right1["subsurface"] = pygame.transform.scale(self.right1["subsurface"], self.size)
        self.right2 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Right 2"]["frame"]["x"],
                        self.tilesetjson["Right 2"]["frame"]["y"],
                        self.tilesetjson["Right 2"]["frame"]["w"],
                        self.tilesetjson["Right 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Right 2"]["duration"]
        }
        self.right2["subsurface"] = pygame.transform.scale(self.right2["subsurface"], self.size)
        self.right3 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Right 3"]["frame"]["x"],
                        self.tilesetjson["Right 3"]["frame"]["y"],
                        self.tilesetjson["Right 3"]["frame"]["w"],
                        self.tilesetjson["Right 3"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Right 3"]["duration"]
        }
        self.right3["subsurface"] = pygame.transform.scale(self.right3["subsurface"], self.size)
        # Shop Left
        self.left0= {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Left 0"]["frame"]["x"],
                        self.tilesetjson["Left 0"]["frame"]["y"],
                        self.tilesetjson["Left 0"]["frame"]["w"],
                        self.tilesetjson["Left 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Left 0"]["duration"]
        }
        self.left0["subsurface"] = pygame.transform.scale(self.left0["subsurface"], self.size)
        self.left1= {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Left 1"]["frame"]["x"],
                        self.tilesetjson["Left 1"]["frame"]["y"],
                        self.tilesetjson["Left 1"]["frame"]["w"],
                        self.tilesetjson["Left 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Left 1"]["duration"]
        }
        self.left1["subsurface"] = pygame.transform.scale(self.left1["subsurface"], self.size)
        self.left2= {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Left 2"]["frame"]["x"],
                        self.tilesetjson["Left 2"]["frame"]["y"],
                        self.tilesetjson["Left 2"]["frame"]["w"],
                        self.tilesetjson["Left 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Left 2"]["duration"]
        }
        self.left2["subsurface"] = pygame.transform.scale(self.left2["subsurface"], self.size)
        self.left3= {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Left 3"]["frame"]["x"],
                        self.tilesetjson["Left 3"]["frame"]["y"],
                        self.tilesetjson["Left 3"]["frame"]["w"],
                        self.tilesetjson["Left 3"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Left 3"]["duration"]
        }
        self.left3["subsurface"] = pygame.transform.scale(self.left3["subsurface"], self.size)

        self.x = x
        self.y = y

        self.right_list = [self.right0, self.right1, self.right2, self.right3]
        self.left_list = [self.left0, self.left1, self.left2, self.left3]

        self.actual_skin = self.right0
        self.frame = 0
        self.last_change = 0

    def change_skin(self, offset_x):
        skin_list = []
        x = main_game.player.x - offset_x
        if x - 150 < self.x:
            skin_list = self.left_list
            if self.actual_skin in self.right_list:
                self.frame = 0
        else:
            skin_list = self.right_list
            if self.actual_skin in self.left_list:
                self.frame = 0
        self.actual_skin = skin_list[self.frame]
        self.frame += 1
        if self.frame > 3:
            self.frame = 0


    def draw(self, surface, ground_altitude, offset_x) :
        now = pygame.time.get_ticks()
        if now - self.last_change > (self.actual_skin["duration"]) :
            self.last_change = now
            self.change_skin(offset_x)
        
        rect = self.actual_skin["subsurface"].get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin["subsurface"], rect)
