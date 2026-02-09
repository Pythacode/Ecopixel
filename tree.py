# -------------------------------- Menu -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la classe arbre.                     #
# Crée par Lucas - https://github.com/GreGrenier                         #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import os
import pygame
import json
from game import*


class Tree():
    def __init__(self, x, y=0, time_alive=0, type=""):
        self.image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "tree", "tree.png"]))

        imageJsonFile = open(os.sep.join([main_game.asset_doc, "image", "tree", "tree_frame.json"]), 'r')
        self.tilesetjson = json.load(imageJsonFile)

        self.size = (256, 256)
        
        # Seedling's Frames
        self.seedling0 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Seedling 0"]["frame"]["x"],
                        self.tilesetjson["Seedling 0"]["frame"]["y"],
                        self.tilesetjson["Seedling 0"]["frame"]["w"],
                        self.tilesetjson["Seedling 0"]["frame"]["h"]
                    )
        }
        self.seedling0["subsurface"] = pygame.transform.scale(self.seedling0["subsurface"], self.size)
        self.seedling1 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Seedling 1"]["frame"]["x"],
                        self.tilesetjson["Seedling 1"]["frame"]["y"],
                        self.tilesetjson["Seedling 1"]["frame"]["w"],
                        self.tilesetjson["Seedling 1"]["frame"]["h"]
                    )
        }
        self.seedling1["subsurface"] = pygame.transform.scale(self.seedling1["subsurface"], self.size)
        self.seedling2 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Seedling 2"]["frame"]["x"],
                        self.tilesetjson["Seedling 2"]["frame"]["y"],
                        self.tilesetjson["Seedling 2"]["frame"]["w"],
                        self.tilesetjson["Seedling 2"]["frame"]["h"]
                    )
        }
        self.seedling2["subsurface"] = pygame.transform.scale(self.seedling2["subsurface"], self.size)
        # Oak's Frames
        self.oak0 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Oak 0"]["frame"]["x"],
                        self.tilesetjson["Oak 0"]["frame"]["y"],
                        self.tilesetjson["Oak 0"]["frame"]["w"],
                        self.tilesetjson["Oak 0"]["frame"]["h"]
                    )
        }
        self.oak0["subsurface"] = pygame.transform.scale(self.oak0["subsurface"], self.size)
        self.oak1 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Oak 1"]["frame"]["x"],
                        self.tilesetjson["Oak 1"]["frame"]["y"],
                        self.tilesetjson["Oak 1"]["frame"]["w"],
                        self.tilesetjson["Oak 1"]["frame"]["h"]
                    )
        }
        self.oak1["subsurface"] = pygame.transform.scale(self.oak1["subsurface"], self.size)
        self.oak2 = {"subsurface" : self.image.subsurface(
                        self.tilesetjson["Oak 2"]["frame"]["x"],
                        self.tilesetjson["Oak 2"]["frame"]["y"],
                        self.tilesetjson["Oak 2"]["frame"]["w"],
                        self.tilesetjson["Oak 2"]["frame"]["h"]
                    )
        }
        self.oak2["subsurface"] = pygame.transform.scale(self.oak2["subsurface"], self.size)


        self.actual_skin = self.seedling0
        self.rect = self.actual_skin["subsurface"].get_rect()

        self.skin_index = 0
        self.seedling_skin_list = (self.seedling0, self.seedling1, self.seedling2)
        self.oak_skin_list = (self.oak0, self.oak1, self.oak2)
        
        self.seedling = True
        self.growned_up = False
        self.type = type

        self.time_alive = time_alive
        self.f = 0

        self.x = x
        self.y = y
    
    def change_skin(self) :
        self.skin_index += 1
        if self.seedling:
            skin_list = self.seedling_skin_list
            if self.skin_index > len(self.seedling_skin_list)-1:
                self.seedling = False
                self.skin_index = 0
                skin_list = self.oak_skin_list
        else:
            if self.type == "oak":
                skin_list = self.oak_skin_list
                if self.skin_index == len(self.oak_skin_list)-1:
                    self.growned_up = True
        self.actual_skin = skin_list[self.skin_index]

    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin["subsurface"].get_rect()
        rect[0], rect[1] = self.x+offset_x, ground_altitude - self.y - self.size[1]
        surface.blit(self.actual_skin["subsurface"], rect)

        self.f += 1 * main_game.dt
        if self.f >= 100 and not self.growned_up:
            self.time_alive +=1
            self.f = 0
            if self.time_alive == 1000:
                self.change_skin()
                self.time_alive = 0
