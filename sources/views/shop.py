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
        
        self.image_arrosoir,self.rect_arrosoir = self.img(288,288, (200, 150),"item","arrosoir.png")
        self.image_rupture_arrosoir,self.rect_rupture_arrosoir = self.img(288,288, (200,150),"shop","Rupture.png")

        self.image_fertilizer,self.rect_fertilizer = self.img(192,192,(450,150),"item","fertilizer.png")
        self.image_rupture_fertilizer,self.rect_rupture_fertilizer = self.img(192,192, (450,150),"shop","Rupture.png")

        self.image_house2,self.rect_house2 = self.img(288,288, (200,450),"houses","house2.png")
        self.image_rupture_house2,self.rect_rupture_house2 = self.img(288,288, (200,450),"shop","Rupture.png")

        self.image_house3,self.rect_house3 = self.img(288,288, (500,450),"houses","house3.png")
        self.image_rupture_house3,self.rect_rupture_house3 = self.img(288,288, (500,450),"shop","Rupture.png")

        self.image_house4,self.rect_house4 = self.img(288,288, (800,450),"houses","house4.png")
        self.image_rupture_house4,self.rect_rupture_house4 = self.img(288,288, (800,450),"shop","Rupture.png")
        
        self.arrosoir_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,300), 192, 192/2, self.Acheter_arrosoir,"Arrosoir")
        self.fertilizer_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (450,300), 192, 192/2, self.Acheter_fertilizer,"Fertilizer")
        self.vendre_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (1160,75), 192+25, 192/3, self.Vendre_item,"Vendre")
        self.upgrade1_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,650), 192, 192/2, self.Amelioration1,"Ameliorer la Maison")
        self.upgrade2_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (450,650), 192, 192/2, self.Amelioration2,"Ameliorer la Maison")
        self.upgrade3_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (720,650), 192, 192/2, self.Amelioration3,"Ameliorer la Maison")


        self.items = json.load(tilsetJsonFile)
        self.header = True
        self.previous_view = None

        self.buy_cooldown = 0

        
    def  update (self,event):
        main_game.screen.fill("#ffe75d")
        main_game.screen.blit(self.image_arrosoir,self.rect_arrosoir)
        main_game.screen.blit(self.image_fertilizer,self.rect_fertilizer)
        main_game.screen.blit(self.image_house2,self.rect_house2)
        self.arrosoir_btn.update(main_game.screen)
        self.fertilizer_btn.update(main_game.screen)
        self.vendre_btn.update(main_game.screen)
        self.upgrade1_btn.update(main_game.screen)
        if self.items[0]["quantity"] == 0:
            main_game.screen.blit(self.image_rupture_arrosoir,self.rect_rupture_arrosoir)
        if self.items[2]["quantity"] == 0:
            main_game.screen.blit(self.image_rupture_house2,self.rect_rupture_house2)
            main_game.screen.blit(self.image_house3,self.rect_house3)
            self.upgrade2_btn.update(main_game.screen)
        if self.items[3]["quantity"] == 0:
            main_game.screen.blit(self.image_rupture_house3,self.rect_rupture_house3)
            main_game.screen.blit(self.image_house4,self.rect_house4)
            self.upgrade3_btn.update(main_game.screen)
        if self.items[4]["quantity"] == 0:
            main_game.screen.blit(self.image_rupture_house4,self.rect_rupture_house4)

    def img(self,width,height,position,dossier,png):
        """
        Données pour la fonction img:

        :param width: Largeur de l'image en int
        :param height: Hauteur de l'image en int
        :param x: Position horizontale de l'image en int
        :param y: Position verticale de l'image en int
        :param path: Chemin dans les fichier de l'image à afficher en str
        """
        # Résultat : Affiche une image sur la fenêtre

        image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", dossier, png]))
        image = pygame.transform.scale(image, (width,height))
        rect = image.get_rect()
        rect.center = position
        return image, rect
    
    def Acheter_arrosoir(self):
        if self.items[0]["quantity"] > 0 and main_game.player.money > self.items[0]['price']:
            self.items[0]["quantity"] -= 1
            main_game.player.money -= self.items[0]["price"]
            main_game.player.arrosoir = True
    
    def Acheter_fertilizer(self):
        if main_game.player.money > self.items[1]['price'] and self.buy_cooldown + 5 * main_game.dt < pygame.time.get_ticks():
            main_game.player.money -= self.items[1]["price"]
            main_game.player.fertilizer += 1
            self.buy_cooldown = pygame.time.get_ticks()

    def Amelioration1(self):
        if self.items[2]["quantity"] > 0 and main_game.player.money > self.items[2]['price']:
            main_game.player.money -= self.items[2]["price"]
            self.items[2]["quantity"] -= 1
            main_game.house.lvl = 2
            main_game.screen.blit(self.image_house3,self.rect_house3)
        
    def Amelioration2(self):
        if self.items[3]["quantity"] > 0 and main_game.player.money > self.items[3]['price']:
            main_game.player.money -= self.items[3]["price"]
            self.items[3]["quantity"] -= 1
            main_game.house.lvl = 3
            main_game.screen.blit(self.image_house3,self.rect_house4)

    def Amelioration3(self):
        if self.items[4]["quantity"] > 0 and main_game.player.money > self.items[4]['price']:
            main_game.player.money -= self.items[4]["price"]
            main_game.house.lvl = 4
            self.items[4]["quantity"] -= 1

    def Vendre_item(self):
        main_game.tuto.next("buy")
        main_game.player.money += self.items[5]["price"]*main_game.player.fruits
        main_game.player.fruits = 0
