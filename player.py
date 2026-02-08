# -------------------------------- Game -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par                                                               #
#          - Titouan - https://github.com/Pythacode/                     #
#          - Lucas - https://github.com/GreGrenier                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import os
import json
import pygame
from game import main_game

class Player() :
    def __init__(self, center):
        self.tileset = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player", "player.png"]))

        tilsetJsonFile = open(os.sep.join([main_game.asset_doc, "image", "player", "player_frame.json"]), 'r')
        self.tilesetjson = json.load(tilsetJsonFile)

        self.size = (120, 228)

        #Handle Animation Frame
        self.idle0 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Idle 0"]["frame"]["x"],
                        self.tilesetjson["Idle 0"]["frame"]["y"],
                        self.tilesetjson["Idle 0"]["frame"]["w"],
                        self.tilesetjson["Idle 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Idle 0"]["duration"]
        }
        self.idle0["subsurface"] = pygame.transform.scale(self.idle0["subsurface"], self.size)
        self.idle1 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Idle 1"]["frame"]["x"],
                        self.tilesetjson["Idle 1"]["frame"]["y"],
                        self.tilesetjson["Idle 1"]["frame"]["w"],
                        self.tilesetjson["Idle 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Idle 1"]["duration"]
        }
        self.idle1["subsurface"] = pygame.transform.scale(self.idle1["subsurface"], self.size)
        self.idle2 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Idle 2"]["frame"]["x"],
                        self.tilesetjson["Idle 2"]["frame"]["y"],
                        self.tilesetjson["Idle 2"]["frame"]["w"],
                        self.tilesetjson["Idle 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Idle 2"]["duration"]
        }
        self.idle2["subsurface"] = pygame.transform.scale(self.idle2["subsurface"], self.size)

        self.run0 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 0"]["frame"]["x"],
                        self.tilesetjson["Run 0"]["frame"]["y"],
                        self.tilesetjson["Run 0"]["frame"]["w"],
                        self.tilesetjson["Run 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 0"]["duration"]
        }
        self.run0["subsurface"] = pygame.transform.scale(self.run0["subsurface"], self.size)
        self.run1 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 1"]["frame"]["x"],
                        self.tilesetjson["Run 1"]["frame"]["y"],
                        self.tilesetjson["Run 1"]["frame"]["w"],
                        self.tilesetjson["Run 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 1"]["duration"]
        }
        self.run1["subsurface"] = pygame.transform.scale(self.run1["subsurface"], self.size)
        self.run2 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 2"]["frame"]["x"],
                        self.tilesetjson["Run 2"]["frame"]["y"],
                        self.tilesetjson["Run 2"]["frame"]["w"],
                        self.tilesetjson["Run 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 2"]["duration"]
        }
        self.run2["subsurface"] = pygame.transform.scale(self.run2["subsurface"], self.size)
        self.run3 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 3"]["frame"]["x"],
                        self.tilesetjson["Run 3"]["frame"]["y"],
                        self.tilesetjson["Run 3"]["frame"]["w"],
                        self.tilesetjson["Run 3"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 3"]["duration"]
        }
        self.run3["subsurface"] = pygame.transform.scale(self.run3["subsurface"], self.size)
        self.run4 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 4"]["frame"]["x"],
                        self.tilesetjson["Run 4"]["frame"]["y"],
                        self.tilesetjson["Run 4"]["frame"]["w"],
                        self.tilesetjson["Run 4"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 4"]["duration"]
        }
        self.run4["subsurface"] = pygame.transform.scale(self.run4["subsurface"], self.size)
        self.run5 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 5"]["frame"]["x"],
                        self.tilesetjson["Run 5"]["frame"]["y"],
                        self.tilesetjson["Run 5"]["frame"]["w"],
                        self.tilesetjson["Run 5"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 5"]["duration"]
        }
        self.run5["subsurface"] = pygame.transform.scale(self.run5["subsurface"], self.size)
        self.run6 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 6"]["frame"]["x"],
                        self.tilesetjson["Run 6"]["frame"]["y"],
                        self.tilesetjson["Run 6"]["frame"]["w"],
                        self.tilesetjson["Run 6"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 6"]["duration"]
        }
        self.run6["subsurface"] = pygame.transform.scale(self.run6["subsurface"], self.size)
        self.run7 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Run 7"]["frame"]["x"],
                        self.tilesetjson["Run 7"]["frame"]["y"],
                        self.tilesetjson["Run 7"]["frame"]["w"],
                        self.tilesetjson["Run 7"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Run 7"]["duration"]
        }
        self.run7["subsurface"] = pygame.transform.scale(self.run7["subsurface"], self.size)


        self.static_skin_list = (self.idle0, self.idle1, self.idle2)
        self.move_skin_list = (self.run0, self.run1, self.run2, self.run3, self.run4, self.run5, self.run6, self.run7)

        self.actual_skin = self.idle0
        self.skin_index = 0

        self.x = center
        self.y = 0
        self.orientation = "RIGHT"

        self.velocity = 1
        self.last_change = pygame.time.get_ticks()
        self.move = False

    def change_skin(self) :
            self.skin_index += 1
            if self.move :
                skin_list = self.move_skin_list
                if self.skin_index > len(self.move_skin_list)-1:
                    self.skin_index = 0
            else :
                skin_list = self.static_skin_list
                if self.skin_index > len(self.static_skin_list)-1:
                    self.skin_index = 0
            self.actual_skin = skin_list[self.skin_index]

    def draw(self, surface, ground_altitude) :
        now = pygame.time.get_ticks()
        if now - self.last_change > (self.actual_skin["duration"]) :
            self.last_change = now
            self.change_skin()
        rect = self.actual_skin["subsurface"].get_rect()
        rect[0], rect[1] = self.x, ground_altitude + self.y - rect[3]
        surface.blit(pygame.transform.flip(self.actual_skin["subsurface"], True, False) if self.orientation == "LEFT" else self.actual_skin["subsurface"], rect)

    def move_left(self, dt) :
        self.move = True
        self.x -= self.velocity * dt

    def move_right(self, dt) :
        self.move = True
        self.x += self.velocity * dt
