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
import tree
from game import main_game

class Player() :
    def __init__(self, center):
        self.tileset = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player", "player.png"]))

        tilsetJsonFile = open(os.sep.join([main_game.asset_doc, "image", "player", "player_frame.json"]), 'r')
        self.tilesetjson = json.load(tilsetJsonFile)

        self.size = (120, 228)

        # Handle Animation Frame
        # Idle Frames
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

        # Run Frames
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
        
        # Plant Frames
        self.plant0 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 0"]["frame"]["x"],
                        self.tilesetjson["Plant 0"]["frame"]["y"],
                        self.tilesetjson["Plant 0"]["frame"]["w"],
                        self.tilesetjson["Plant 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 0"]["duration"]
        }
        self.plant0["subsurface"] = pygame.transform.scale(self.plant0["subsurface"], self.size)
        self.plant1 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 1"]["frame"]["x"],
                        self.tilesetjson["Plant 1"]["frame"]["y"],
                        self.tilesetjson["Plant 1"]["frame"]["w"],
                        self.tilesetjson["Plant 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 1"]["duration"]
        }
        self.plant1["subsurface"] = pygame.transform.scale(self.plant1["subsurface"], self.size)
        self.plant2 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 2"]["frame"]["x"],
                        self.tilesetjson["Plant 2"]["frame"]["y"],
                        self.tilesetjson["Plant 2"]["frame"]["w"],
                        self.tilesetjson["Plant 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 2"]["duration"]
        }
        self.plant2["subsurface"] = pygame.transform.scale(self.plant2["subsurface"], self.size)
        self.plant3 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 3"]["frame"]["x"],
                        self.tilesetjson["Plant 3"]["frame"]["y"],
                        self.tilesetjson["Plant 3"]["frame"]["w"],
                        self.tilesetjson["Plant 3"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 3"]["duration"]
        }
        self.plant3["subsurface"] = pygame.transform.scale(self.plant3["subsurface"], self.size)
        self.plant4 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 4"]["frame"]["x"],
                        self.tilesetjson["Plant 4"]["frame"]["y"],
                        self.tilesetjson["Plant 4"]["frame"]["w"],
                        self.tilesetjson["Plant 4"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 4"]["duration"]
        }
        self.plant4["subsurface"] = pygame.transform.scale(self.plant4["subsurface"], self.size)
        self.plant5 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 5"]["frame"]["x"],
                        self.tilesetjson["Plant 5"]["frame"]["y"],
                        self.tilesetjson["Plant 5"]["frame"]["w"],
                        self.tilesetjson["Plant 5"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 5"]["duration"]
        }
        self.plant5["subsurface"] = pygame.transform.scale(self.plant5["subsurface"], self.size)
        self.plant6 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 6"]["frame"]["x"],
                        self.tilesetjson["Plant 6"]["frame"]["y"],
                        self.tilesetjson["Plant 6"]["frame"]["w"],
                        self.tilesetjson["Plant 6"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 6"]["duration"]
        }
        self.plant6["subsurface"] = pygame.transform.scale(self.plant6["subsurface"], self.size)
        self.plant7 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 7"]["frame"]["x"],
                        self.tilesetjson["Plant 7"]["frame"]["y"],
                        self.tilesetjson["Plant 7"]["frame"]["w"],
                        self.tilesetjson["Plant 7"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 7"]["duration"]
        }
        self.plant7["subsurface"] = pygame.transform.scale(self.plant7["subsurface"], self.size)
        self.plant8 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 8"]["frame"]["x"],
                        self.tilesetjson["Plant 8"]["frame"]["y"],
                        self.tilesetjson["Plant 8"]["frame"]["w"],
                        self.tilesetjson["Plant 8"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 8"]["duration"]
        }
        self.plant8["subsurface"] = pygame.transform.scale(self.plant8["subsurface"], self.size)
        self.plant9 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 9"]["frame"]["x"],
                        self.tilesetjson["Plant 9"]["frame"]["y"],
                        self.tilesetjson["Plant 9"]["frame"]["w"],
                        self.tilesetjson["Plant 9"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 9"]["duration"]
        }
        self.plant9["subsurface"] = pygame.transform.scale(self.plant9["subsurface"], self.size)
        self.plant10 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 10"]["frame"]["x"],
                        self.tilesetjson["Plant 10"]["frame"]["y"],
                        self.tilesetjson["Plant 10"]["frame"]["w"],
                        self.tilesetjson["Plant 10"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 10"]["duration"]
        }
        self.plant10["subsurface"] = pygame.transform.scale(self.plant10["subsurface"], self.size)
        self.plant11 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 11"]["frame"]["x"],
                        self.tilesetjson["Plant 11"]["frame"]["y"],
                        self.tilesetjson["Plant 11"]["frame"]["w"],
                        self.tilesetjson["Plant 11"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 11"]["duration"]
        }
        self.plant11["subsurface"] = pygame.transform.scale(self.plant11["subsurface"], self.size)
        self.plant12 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 12"]["frame"]["x"],
                        self.tilesetjson["Plant 12"]["frame"]["y"],
                        self.tilesetjson["Plant 12"]["frame"]["w"],
                        self.tilesetjson["Plant 12"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 12"]["duration"]
        }
        self.plant12["subsurface"] = pygame.transform.scale(self.plant12["subsurface"], self.size)
        self.plant13 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 13"]["frame"]["x"],
                        self.tilesetjson["Plant 13"]["frame"]["y"],
                        self.tilesetjson["Plant 13"]["frame"]["w"],
                        self.tilesetjson["Plant 13"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 13"]["duration"]
        }
        self.plant13["subsurface"] = pygame.transform.scale(self.plant13["subsurface"], self.size)
        self.plant14 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Plant 14"]["frame"]["x"],
                        self.tilesetjson["Plant 14"]["frame"]["y"],
                        self.tilesetjson["Plant 14"]["frame"]["w"],
                        self.tilesetjson["Plant 14"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Plant 14"]["duration"]
        }
        self.plant14["subsurface"] = pygame.transform.scale(self.plant14["subsurface"], self.size)

        self.static_skin_list = (self.idle0, self.idle1, self.idle2)
        self.move_skin_list = (self.run0, self.run1, self.run2, self.run3, self.run4, self.run5, self.run6, self.run7)
        self.plant_skin_list = (self.plant0, self.plant1, self.plant2, self.plant3, self.plant4, self.plant5, self.plant6, self.plant7, self.plant8, self.plant9, self.plant10, self.plant11, self.plant12, self.plant13, self.plant14)

        playerdata = main_game.data.get('player', {})

        self.actual_skin = self.idle0
        self.skin_index = playerdata.get('skin_index', 0)

        self.x = playerdata.get('x', center)
        self.y = playerdata.get('y', 0)
        self.orientation = playerdata.get('orientation', 'RIGHT')

        self.velocity = 1
        self.last_change = pygame.time.get_ticks()
        self.move = False
        self.plant = playerdata.get('plant', False)

        self.money = playerdata.get('money', 0)
        self.sprout = playerdata.get('sprout', 0)

    def change_skin(self) :
            self.skin_index += 1
            if self.plant:
                skin_list = self.plant_skin_list
                if self.skin_index > len(self.plant_skin_list)-1:
                    self.skin_index = 0
                    self.plant = False
                elif self.skin_index == 11 :
                    main_game.game_view.draw_element.append(main_game.game_view.wait_tree)
                    main_game.game_view.wait_tree = None
            elif self.move:
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
    
    def plant_act(self):
        self.plant = True

    def move_left(self) :
        self.move = True
        self.x -= self.velocity * main_game.dt

    def move_right(self) :
        self.move = True
        self.x += self.velocity * main_game.dt
