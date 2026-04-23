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
    "dirt": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "ground.png"])), "size":(32,32), "price" : 32},
    "fruits": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "fruits.png"])), "size":(32,32), "price" : 32},
    "logo": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "logo.png"])), "size":(32,32), "price" : 32},
    "sprout": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "sprout.png"])), "size":(32,32), "price" : 32},
    "arrosoir": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "item", "arrosoir.png"])), "size":(32,32), "price" : 32},
    "table": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "decoration", "table.png"])), "size":(32,10), "price" : 32},
    "fence": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "decoration", "fence.png"])), "size":(32,16), "price" : 32},
    "flowerpot": {"img":pygame.image.load(os.sep.join([main_game.asset_doc, "image", "decoration", "flowerpot.png"])), "size":(12,24), "price" : 32}
}

list_decoration_type = list(decoration_type.keys())

class Decoration():
    def __init__(self):

        self.x = self.y = None
        self.placed = False
        self.change_type((main_game.scroll_y//10)%len(decoration_type))
    
    def draw(self, surface, ground_altitude, offset_x) :
        rect = self.actual_skin.get_rect()
        if not self.placed : 
            rect.center = pygame.mouse.get_pos()
        else :
            rect.center = self.x + offset_x, ground_altitude - self.y - 32
        surface.blit(self.actual_skin, rect)

    def change_type(self, type) :
        type = list_decoration_type[type]
        self.type = type
        self.actual_skin = decoration_type[self.type]["img"]
        self.actual_skin = pygame.transform.scale(self.actual_skin, decoration_type[self.type]["size"])
        self.size = decoration_type[self.type]["size"]
        self.actual_skin.set_alpha(200)

    def placing(self, offset_x, ground_height):
        if main_game.player.money >= decoration_type[self.type]["price"] :
            main_game.player.money -= decoration_type[self.type]["price"]
            self.x = pygame.mouse.get_pos()[0] - offset_x
            self.y = (main_game.screen.get_size()[1] - pygame.mouse.get_pos()[1] - ground_height) - decoration_type[self.type]["size"][1]
            self.actual_skin.set_alpha(255)
            self.placed = True
            return True
        else :
            main_game.player.say('Je suis trop pauvre :/', 2000)
            return False

