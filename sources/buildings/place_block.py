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

decoration_type = {
    "dirt": {"dir":[main_game.asset_doc, "image", "game", "ground.png"], "size":(32,32)},
    "fruits": {"dir":[main_game.asset_doc, "image", "game", "fruits.png"], "size":(32,32)},
    "logo": {"dir":[main_game.asset_doc, "image", "game", "logo.png"], "size":(32,32)},
    "sprout": {"dir":[main_game.asset_doc, "image", "game", "sprout.png"], "size":(32,32)},
    "arrosoir": {"dir":[main_game.asset_doc, "image", "item", "arrosoir.png"], "size":(32,32)},
    "table": {"dir":[main_game.asset_doc, "image", "decoration", "table.png"], "size":(32,10)},
    "fence": {"dir":[main_game.asset_doc, "image", "decoration", "fence.png"], "size":(32,16)},
    "flowerpot": {"dir":[main_game.asset_doc, "image", "decoration", "flowerpot.png"], "size":(12,24)}
}

class Decoration():
    def __init__(self):

        self.x = self.y = None
        self.placed = False
        self.type = list(decoration_type.keys())[0]
        self.actual_skin = pygame.image.load(os.sep.join(decoration_type[self.type]["dir"]))
        self.actual_skin = pygame.transform.scale(self.actual_skin, decoration_type[self.type]["size"])
        self.size = decoration_type[self.type]["size"]
        self.actual_skin.set_alpha(200)
    
    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        if not self.placed : 
            rect.center = pygame.mouse.get_pos()
        else :
            rect.center = self.x + offset_x, ground_altitude - self.y - 32
        surface.blit(self.actual_skin, rect)

    def placing(self, offset_x, ground_height):
        self.x = pygame.mouse.get_pos()[0] - offset_x
        self.y = (main_game.screen.get_size()[1] - pygame.mouse.get_pos()[1] - ground_height) - decoration_type[self.type]["size"][1]
        self.actual_skin.set_alpha(255)
        self.placed = True

