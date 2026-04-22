# ------------------------------- Player ------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par                                                               #
#          - Titouan - https://github.com/Pythacode/                     #
#          - Lucas - https://github.com/GreGrenier/                      #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import json
import pygame
from sprites.tree import Tree
from game import *
from tuto import Tuto

class Player() :
    def __init__(self, center, playerdata=None, pnj=False):
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
        self.washeddown0 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 0"]["frame"]["x"],
                        self.tilesetjson["Washeddown 0"]["frame"]["y"],
                        self.tilesetjson["Washeddown 0"]["frame"]["w"],
                        self.tilesetjson["Washeddown 0"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 0"]["duration"]
        }
        self.washeddown0["subsurface"] = pygame.transform.scale(self.washeddown0["subsurface"], self.size)
        self.washeddown1 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 1"]["frame"]["x"],
                        self.tilesetjson["Washeddown 1"]["frame"]["y"],
                        self.tilesetjson["Washeddown 1"]["frame"]["w"],
                        self.tilesetjson["Washeddown 1"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 1"]["duration"]
        }
        self.washeddown1["subsurface"] = pygame.transform.scale(self.washeddown1["subsurface"], self.size)
        self.washeddown2 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 2"]["frame"]["x"],
                        self.tilesetjson["Washeddown 2"]["frame"]["y"],
                        self.tilesetjson["Washeddown 2"]["frame"]["w"],
                        self.tilesetjson["Washeddown 2"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 2"]["duration"]
        }
        self.washeddown2["subsurface"] = pygame.transform.scale(self.washeddown2["subsurface"], self.size)
        self.washeddown3 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 3"]["frame"]["x"],
                        self.tilesetjson["Washeddown 3"]["frame"]["y"],
                        self.tilesetjson["Washeddown 3"]["frame"]["w"],
                        self.tilesetjson["Washeddown 3"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 3"]["duration"]
        }
        self.washeddown3["subsurface"] = pygame.transform.scale(self.washeddown3["subsurface"], self.size)
        self.washeddown4 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 4"]["frame"]["x"],
                        self.tilesetjson["Washeddown 4"]["frame"]["y"],
                        self.tilesetjson["Washeddown 4"]["frame"]["w"],
                        self.tilesetjson["Washeddown 4"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 4"]["duration"]
        }
        self.washeddown4["subsurface"] = pygame.transform.scale(self.washeddown4["subsurface"], self.size)
        self.washeddown5 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 5"]["frame"]["x"],
                        self.tilesetjson["Washeddown 5"]["frame"]["y"],
                        self.tilesetjson["Washeddown 5"]["frame"]["w"],
                        self.tilesetjson["Washeddown 5"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 5"]["duration"]
        }
        self.washeddown5["subsurface"] = pygame.transform.scale(self.washeddown5["subsurface"], self.size)
        self.washeddown6 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 6"]["frame"]["x"],
                        self.tilesetjson["Washeddown 6"]["frame"]["y"],
                        self.tilesetjson["Washeddown 6"]["frame"]["w"],
                        self.tilesetjson["Washeddown 6"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 6"]["duration"]
        }
        self.washeddown6["subsurface"] = pygame.transform.scale(self.washeddown6["subsurface"], self.size)
        self.washeddown7 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 7"]["frame"]["x"],
                        self.tilesetjson["Washeddown 7"]["frame"]["y"],
                        self.tilesetjson["Washeddown 7"]["frame"]["w"],
                        self.tilesetjson["Washeddown 7"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 7"]["duration"]
        }
        self.washeddown7["subsurface"] = pygame.transform.scale(self.washeddown7["subsurface"], self.size)
        self.washeddown8 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 8"]["frame"]["x"],
                        self.tilesetjson["Washeddown 8"]["frame"]["y"],
                        self.tilesetjson["Washeddown 8"]["frame"]["w"],
                        self.tilesetjson["Washeddown 8"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 8"]["duration"]
        }
        self.washeddown8["subsurface"] = pygame.transform.scale(self.washeddown8["subsurface"], self.size)
        self.washeddown9 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 9"]["frame"]["x"],
                        self.tilesetjson["Washeddown 9"]["frame"]["y"],
                        self.tilesetjson["Washeddown 9"]["frame"]["w"],
                        self.tilesetjson["Washeddown 9"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 9"]["duration"]
        }
        self.washeddown9["subsurface"] = pygame.transform.scale(self.washeddown9["subsurface"], self.size)
        self.washeddown10 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 10"]["frame"]["x"],
                        self.tilesetjson["Washeddown 10"]["frame"]["y"],
                        self.tilesetjson["Washeddown 10"]["frame"]["w"],
                        self.tilesetjson["Washeddown 10"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 10"]["duration"]
        }
        self.washeddown10["subsurface"] = pygame.transform.scale(self.washeddown10["subsurface"], self.size)
        self.washeddown11 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 11"]["frame"]["x"],
                        self.tilesetjson["Washeddown 11"]["frame"]["y"],
                        self.tilesetjson["Washeddown 11"]["frame"]["w"],
                        self.tilesetjson["Washeddown 11"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 11"]["duration"]
        }
        self.washeddown11["subsurface"] = pygame.transform.scale(self.washeddown11["subsurface"], self.size)
        self.washeddown12 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 12"]["frame"]["x"],
                        self.tilesetjson["Washeddown 12"]["frame"]["y"],
                        self.tilesetjson["Washeddown 12"]["frame"]["w"],
                        self.tilesetjson["Washeddown 12"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 12"]["duration"]
        }
        self.washeddown12["subsurface"] = pygame.transform.scale(self.washeddown12["subsurface"], self.size)
        self.washeddown13 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 13"]["frame"]["x"],
                        self.tilesetjson["Washeddown 13"]["frame"]["y"],
                        self.tilesetjson["Washeddown 13"]["frame"]["w"],
                        self.tilesetjson["Washeddown 13"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 13"]["duration"]
        }
        self.washeddown13["subsurface"] = pygame.transform.scale(self.washeddown13["subsurface"], self.size)
        self.washeddown14 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 14"]["frame"]["x"],
                        self.tilesetjson["Washeddown 14"]["frame"]["y"],
                        self.tilesetjson["Washeddown 14"]["frame"]["w"],
                        self.tilesetjson["Washeddown 14"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 14"]["duration"]
        }
        self.washeddown14["subsurface"] = pygame.transform.scale(self.washeddown14["subsurface"], self.size)
        self.washeddown15 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 15"]["frame"]["x"],
                        self.tilesetjson["Washeddown 15"]["frame"]["y"],
                        self.tilesetjson["Washeddown 15"]["frame"]["w"],
                        self.tilesetjson["Washeddown 15"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 15"]["duration"]
        }
        self.washeddown15["subsurface"] = pygame.transform.scale(self.washeddown15["subsurface"], self.size)
        self.washeddown16 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 16"]["frame"]["x"],
                        self.tilesetjson["Washeddown 16"]["frame"]["y"],
                        self.tilesetjson["Washeddown 16"]["frame"]["w"],
                        self.tilesetjson["Washeddown 16"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 16"]["duration"]
        }
        self.washeddown16["subsurface"] = pygame.transform.scale(self.washeddown16["subsurface"], self.size)
        self.washeddown17 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 17"]["frame"]["x"],
                        self.tilesetjson["Washeddown 17"]["frame"]["y"],
                        self.tilesetjson["Washeddown 17"]["frame"]["w"],
                        self.tilesetjson["Washeddown 17"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 17"]["duration"]
        }
        self.washeddown17["subsurface"] = pygame.transform.scale(self.washeddown17["subsurface"], self.size)
        self.washeddown18 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 18"]["frame"]["x"],
                        self.tilesetjson["Washeddown 18"]["frame"]["y"],
                        self.tilesetjson["Washeddown 18"]["frame"]["w"],
                        self.tilesetjson["Washeddown 18"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 18"]["duration"]
        }
        self.washeddown18["subsurface"] = pygame.transform.scale(self.washeddown18["subsurface"], self.size)
        self.washeddown19 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 19"]["frame"]["x"],
                        self.tilesetjson["Washeddown 19"]["frame"]["y"],
                        self.tilesetjson["Washeddown 19"]["frame"]["w"],
                        self.tilesetjson["Washeddown 19"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 19"]["duration"]
        }
        self.washeddown19["subsurface"] = pygame.transform.scale(self.washeddown19["subsurface"], self.size)
        self.washeddown20 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 20"]["frame"]["x"],
                        self.tilesetjson["Washeddown 20"]["frame"]["y"],
                        self.tilesetjson["Washeddown 20"]["frame"]["w"],
                        self.tilesetjson["Washeddown 20"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 20"]["duration"]
        }
        self.washeddown20["subsurface"] = pygame.transform.scale(self.washeddown20["subsurface"], self.size)
        self.washeddown21 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 21"]["frame"]["x"],
                        self.tilesetjson["Washeddown 21"]["frame"]["y"],
                        self.tilesetjson["Washeddown 21"]["frame"]["w"],
                        self.tilesetjson["Washeddown 21"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 21"]["duration"]
        }
        self.washeddown21["subsurface"] = pygame.transform.scale(self.washeddown21["subsurface"], self.size)
        self.washeddown22 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 22"]["frame"]["x"],
                        self.tilesetjson["Washeddown 22"]["frame"]["y"],
                        self.tilesetjson["Washeddown 22"]["frame"]["w"],
                        self.tilesetjson["Washeddown 22"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 22"]["duration"]
        }
        self.washeddown22["subsurface"] = pygame.transform.scale(self.washeddown22["subsurface"], self.size)
        self.washeddown23 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 23"]["frame"]["x"],
                        self.tilesetjson["Washeddown 23"]["frame"]["y"],
                        self.tilesetjson["Washeddown 23"]["frame"]["w"],
                        self.tilesetjson["Washeddown 23"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 23"]["duration"]
        }
        self.washeddown23["subsurface"] = pygame.transform.scale(self.washeddown23["subsurface"], self.size)
        self.washeddown24 = {"subsurface" : self.tileset.subsurface(
                        self.tilesetjson["Washeddown 24"]["frame"]["x"],
                        self.tilesetjson["Washeddown 24"]["frame"]["y"],
                        self.tilesetjson["Washeddown 24"]["frame"]["w"],
                        self.tilesetjson["Washeddown 24"]["frame"]["h"]
                    ),
                    "duration": self.tilesetjson["Washeddown 24"]["duration"]
        }
        self.washeddown24["subsurface"] = pygame.transform.scale(self.washeddown24["subsurface"], self.size)
        

        self.static_skin_list = (self.idle0, self.idle1, self.idle2)
        self.move_skin_list = (self.run0, self.run1, self.run2, self.run3, self.run4, self.run5, self.run6, self.run7)
        self.plant_skin_list = (self.plant0, self.plant1, self.plant2, self.plant3, self.plant4, self.plant5, self.plant6, self.plant7, self.plant8, self.plant9, self.plant10, self.plant11, self.plant12, self.plant13, self.plant14)
        self.washed_skin_list = (self.washeddown0, self.washeddown1, self.washeddown2, self.washeddown3, self.washeddown4, self.washeddown5, self.washeddown6, self.washeddown7, self.washeddown8, self.washeddown9, self.washeddown10, self.washeddown11, self.washeddown12, self.washeddown13, self.washeddown14, self.washeddown15, self.washeddown16, self.washeddown17, self.washeddown18, self.washeddown19, self.washeddown20, self.washeddown21, self.washeddown22, self.washeddown23, self.washeddown24)

        if playerdata is None :
            if os.path.exists(os.sep.join([main_game.jsonPath, "sauv_game.json"])) :
                playerdata = open(os.sep.join([main_game.jsonPath, "sauv_game.json"]), 'r')
                playerdata = json.load(playerdata).get('player', {})
            else :
                playerdata = {}

        self.actual_skin = self.idle0
        self.skin_index = playerdata.get('skin_index', 0)

        self.x = playerdata.get('x', center)
        self.y = playerdata.get('y', 0)
        self.orientation = playerdata.get('orientation', 'RIGHT')

        self.velocity = 1
        self.last_change = pygame.time.get_ticks()
        self.move = False
        self.plant = playerdata.get('plant', False)
        self.washing = False

        self.money = playerdata.get('money', 0)
        self.sprout = playerdata.get('sprout', 0)
        self.fertilizer = playerdata.get('fertilizer', 0)
        self.fruits = playerdata.get('fruits', 0)
        self.arrosoir = playerdata.get('arrosoir', False)

        self.msg = []
        if not pnj :
            main_game.tuto = Tuto(playerdata.get('tuto_advancement', 0))

        self.pnj = pnj
        self.username = playerdata.get('username', "Singleplayer")

    def say(self, msg, duration):
        self.msg.append({
            'msg' : msg,
            'created' : pygame.time.get_ticks(),
            'duration' : duration
        })

    def change_skin(self) :
            self.skin_index += 1
            if self.plant:
                skin_list = self.plant_skin_list
                if self.skin_index > len(self.plant_skin_list)-1:
                    self.skin_index = 0
                    self.plant = False
                elif self.skin_index == 11 :
                    main_game.game_view.trees.append(Tree(main_game.game_view.wait_tree.get('x'), main_game.game_view.wait_tree.get('y'), main_game.game_view.wait_tree.get('type'), main_game.game_view.wait_tree.get('fertilized')))
                    main_game.game_view.wait_tree = None
            elif self.washing:
                skin_list = self.washed_skin_list
                if self.skin_index > len(self.washed_skin_list)-1:
                    self.skin_index = 0
                    self.washing = False
            elif self.move:
                skin_list = self.move_skin_list
                if self.skin_index > len(self.move_skin_list)-1:
                    self.skin_index = 0
            else :
                skin_list = self.static_skin_list
                if self.skin_index > len(self.static_skin_list)-1:
                    self.skin_index = 0
            self.actual_skin = skin_list[self.skin_index]

    def get_relativ_x(self, offset_x) -> int :
        return self.x + offset_x
            
    def draw(self, surface, ground_altitude, offset_x) :
        now = pygame.time.get_ticks()
        if now - self.last_change > (self.actual_skin["duration"]) :
            self.last_change = now
            self.change_skin()

        rect = self.actual_skin["subsurface"].get_rect()
        y = ground_altitude - self.y - rect[3]
        x = self.get_relativ_x(offset_x)
        rect[0], rect[1] = x, y
        surface.blit(pygame.transform.flip(self.actual_skin["subsurface"], True, False) if self.orientation == "LEFT" else self.actual_skin["subsurface"], rect)
        
        if self.pnj :
            font = pygame.font.Font(main_game.main_font_name, 14)
            h, w = size_text(self.username, font, 300)
            padding = 10
            rect_w = w + 2*padding
            start_pos = x + rect[2]/2-rect_w/2
            #pygame.draw.rect(main_game.screen, (0, 0, 0, 0.5), (start_pos, y-h+10, rect_w, h+10))
            
            pseudo_backround = pygame.Surface((rect_w, h+10))
            pseudo_backround.set_alpha(128)
            pseudo_backround.fill((0, 0, 0))

            pseudo_background_rect = pseudo_backround.get_rect()
            pseudo_background_rect[0], pseudo_background_rect[1] = start_pos, y-h+10

            main_game.screen.blit(pseudo_backround, pseudo_background_rect)
            blit_text(self.username, (start_pos + padding, y-h+15), font, 300, 'white', main_game.screen)

        if len(self.msg) != 0 :
            msg = self.msg[0]
            font = pygame.font.Font(main_game.main_font_name, 24)
            h, w = size_text(msg.get('msg'), font, 300)
            padding = 10
            rect_w = w + 2*padding
            start_pos = x + rect[2]/2-rect_w/2
            pygame.draw.rect(main_game.screen, 'white', (start_pos, y-h+10, rect_w, h+10), 0, 20)
            pygame.draw.rect(main_game.screen, 'black', (start_pos, y-h+10, rect_w, h+10), 3, 20)
            blit_text(msg.get('msg'), (start_pos + padding, y-h+10), font, 300, 'black', main_game.screen)
            if now - msg.get('created') > msg.get('duration') :
                del self.msg[0]
                if len(self.msg) != 0 : 
                    self.msg[0]['created'] = now

    def plant_act(self):
        self.plant = True

    def move_left(self) :
        #self.move = True
        if self.get_relativ_x(main_game.game_view.offset_x) < 200 and not self.pnj :
            main_game.game_view.offset_x += self.velocity * main_game.dt
        self.x -= self.velocity * main_game.dt

    def move_right(self) :
        #self.move = True
        width = main_game.screen.get_size()[0]
        if self.get_relativ_x(main_game.game_view.offset_x) > width - self.size[0] - 200 and not self.pnj :
            main_game.game_view.offset_x -= self.velocity * main_game.dt
        self.x += self.velocity * main_game.dt
