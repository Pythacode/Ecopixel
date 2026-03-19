# -------------------------------- Shop -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Pierrick - https://github.com/PtitBillyboy                    #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import os
import json
from game import*


class shopView():
    def __init__ (self):
        tilsetJsonFile = open(os.sep.join([main_game.asset_doc, "image", "item", "items.json"]))
        self.items = json.load(tilsetJsonFile)
        self.header = True
        self.previous_view = None
        
        
        self.image_arrosoir,self.rect_arrosoir = img(160*1.5,160, (200, 150),"item","arrosoir.png")
        self.image_rupture_arrosoir,self.rect_rupture_arrosoir = img(288,288, (200,150),"shop","Rupture.png")

        self.image_fertilizer,self.rect_fertilizer = img(192,192,(600,150),"item","fertilizer.png")
        self.image_rupture_fertilizer,self.rect_rupture_fertilizer = img(192,192, (600,150),"shop","Rupture.png")

        self.image_house2,self.rect_house2 = img(288,288, (200,450),"houses","house2.png")
        self.image_rupture_house2,self.rect_rupture_house2 = img(288,288, (200,450),"shop","Rupture.png")

        self.image_house3,self.rect_house3 = img(288,288, (600,450),"houses","house3.png")
        self.image_rupture_house3,self.rect_rupture_house3 = img(288,288, (600,450),"shop","Rupture.png")

        self.image_house4,self.rect_house4 = img(288,288, (1000,450),"houses","house4.png")
        self.image_rupture_house4,self.rect_rupture_house4 = img(288,288, (1000,450),"shop","Rupture.png")
        
        self.arrosoir_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,300), 192, 192/2, self.Acheter_arrosoir,"Arrosoir")
        self.fertilizer_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (600,300), 192, 192/2, self.Acheter_fertilizer,"Fertilizer")
        self.vendre_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (1160,75), 192+25, 192/3, self.Vendre_item,"Vendre")
        self.upgrade1_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,650), 192, 192/2, self.Amelioration1,"Ameliorer la Maison")
        self.upgrade2_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (600,650), 192, 192/2, self.Amelioration2,"Ameliorer la Maison")
        self.upgrade3_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (1000,650), 192, 192/2, self.Amelioration3,"Ameliorer la Maison")
        self.Retour_btn = button(os.sep.join([main_game.asset_doc, "image", "icon", "back.png"]), os.sep.join([main_game.asset_doc, "image", "icon", "back.png"]), os.sep.join([main_game.asset_doc, "image", "icon", "back.png"]), (40,60), 50, 50/2, self.Retour,"")

        self.prix_arrosoir_btn = button(os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), (400,150), 50, 50/2, self.Rien,"prix : "+str(self.items[0]["price"]))
        self.prix_fertilizer_btn = button(os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), (800,150), 50, 50/2, self.Rien,"prix : "+str(self.items[1]["price"]))
        self.prix_upgrade1_btn = button(os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), (400,450), 50, 50/2, self.Rien,"prix : "+str(self.items[2]["price"]))
        self.prix_upgrade2_btn = button(os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), (800,450), 50, 50/2, self.Rien,"prix : "+str(self.items[3]["price"]))
        self.prix_upgrade3_btn = button(os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), os.sep.join([main_game.asset_doc, "image", "item", "fond.png"]), (1200,450), 50, 50/2, self.Rien,"prix : "+str(self.items[4]["price"]))

        self.buy_cooldown = 0

        
    def  update (self,event):
        main_game.screen.fill("#ffe75d")
        main_game.screen.blit(self.image_arrosoir,self.rect_arrosoir)
        main_game.screen.blit(self.image_fertilizer,self.rect_fertilizer)
        main_game.screen.blit(self.image_house2,self.rect_house2)
        self.arrosoir_btn.update(main_game.screen)
        self.prix_arrosoir_btn.update(main_game.screen)
        self.fertilizer_btn.update(main_game.screen)
        self.prix_fertilizer_btn.update(main_game.screen)
        self.vendre_btn.update(main_game.screen)
        self.upgrade1_btn.update(main_game.screen)
        self.prix_upgrade1_btn.update(main_game.screen)
        self.Retour_btn.update(main_game.screen)
        if main_game.player.arrosoir == True:
            main_game.screen.blit(self.image_rupture_arrosoir,self.rect_rupture_arrosoir)
        if main_game.house.lvl >= 2:
            main_game.screen.blit(self.image_rupture_house2,self.rect_rupture_house2)
            main_game.screen.blit(self.image_house3,self.rect_house3)
            self.upgrade2_btn.update(main_game.screen)
            self.prix_upgrade2_btn.update(main_game.screen)
        if main_game.house.lvl >= 3:
            main_game.screen.blit(self.image_rupture_house3,self.rect_rupture_house3)
            main_game.screen.blit(self.image_house4,self.rect_house4)
            self.upgrade3_btn.update(main_game.screen)
            self.prix_upgrade3_btn.update(main_game.screen)
        if main_game.house.lvl == 4:
            main_game.screen.blit(self.image_rupture_house4,self.rect_rupture_house4)

    
    def Acheter_arrosoir(self):
        if main_game.player.arrosoir == False and main_game.player.money > self.items[0]['price']:
            main_game.player.money -= self.items[0]["price"]
            main_game.player.arrosoir = True
    
    def Acheter_fertilizer(self):
        if main_game.player.money > self.items[1]['price'] and self.buy_cooldown + 5 * main_game.dt < pygame.time.get_ticks():
            main_game.player.money -= self.items[1]["price"]
            main_game.player.fertilizer += 1
            self.buy_cooldown = pygame.time.get_ticks()

    def Amelioration1(self):
        if main_game.house.lvl == 1 and main_game.player.money > self.items[2]['price']:
            main_game.player.money -= self.items[2]["price"]
            main_game.house.lvl = 2
            main_game.screen.blit(self.image_house3,self.rect_house3)
        
    def Amelioration2(self):
        if main_game.house.lvl == 2 and main_game.player.money > self.items[3]['price']:
            main_game.player.money -= self.items[3]["price"]
            main_game.house.lvl = 3
            main_game.screen.blit(self.image_house3,self.rect_house4)

    def Amelioration3(self):
        if main_game.house.lvl == 3 and main_game.player.money > self.items[4]['price']:
            main_game.player.money -= self.items[4]["price"]
            main_game.house.lvl = 4

    def Vendre_item(self):
        main_game.tuto.next("buy")
        main_game.player.money += self.items[5]["price"]*main_game.player.fruits
        main_game.player.fruits = 0

    def Retour(self):
        main_game.save()
        main_game.change_view(self.previous_view)

    def Rien(self):
        return None