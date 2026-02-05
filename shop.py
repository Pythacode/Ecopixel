import os
import json
from game import*

class shopView():
    def __init__ (self):
        tilsetJsonFile = open(os.sep.join([main_game.asset_doc,"item.Json"]))
        self.items = json.load(tilsetJsonFile)


    def  update (self,event):
        main_game.screen.fill("#ffe75d")
