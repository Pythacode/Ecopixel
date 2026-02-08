# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Pierrick - https://github.com/PtitBillyboy                    #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import os
import json
from game import*

class shopView():
    def __init__ (self):
        tilsetJsonFile = open(os.sep.join([main_game.asset_doc, "shop", "items.json"]))
        self.items = json.load(tilsetJsonFile)


    def  update (self,event):
        main_game.screen.fill("#ffe75d")
