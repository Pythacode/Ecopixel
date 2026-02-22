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
        self.image_house2,self.rect_house2 = self.img(288,288, (200,450),"houses","house2.png")
        self.image_house3,self.rect_house3 = self.img(288,288, (500,450),"houses","house3.png")
        self.image_house4,self.rect_house4 = self.img(288,288, (800,450),"houses","house4.png")
        self.image_rupture,self.rect_rupture = self.img(288,288, (200,150),"shop","Rupture.png")
        self.image_arrosoir,self.rect_arrosoir = self.img(288,288, (200, 150),"item","arrosoir.png")
        self.image_engrais,self.rect_engrais = self.img(192,192,(450,150),"item","engrais.png")

        self.arrosoir_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,300), 192, 192/2, self.Fonction_quand_on_clique,"Arrosoir")
        self.engrais_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (450,300), 192, 192/2, self.Fonction_quand_on_clique,"Engrais")
        self.vendre_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (1160,75), 192+25, 192/3, self.Fonction_quand_on_clique,"Vendre")
        self.upgrade_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,650), 192, 192/2, self.Amelioration,"Ameliorer la Maison")

        self.items = json.load(tilsetJsonFile)
        self.header = True
        self.previous_view = None

        
    def  update (self,event):
        main_game.screen.fill("#ffe75d")
        main_game.screen.blit(self.image_arrosoir,self.rect_arrosoir)
        main_game.screen.blit(self.image_engrais,self.rect_engrais)
        main_game.screen.blit(self.image_house2,self.rect_house2)
        self.arrosoir_btn.update(main_game.screen)
        self.engrais_btn.update(main_game.screen)
        self.vendre_btn.update(main_game.screen)
        self.upgrade_btn.update(main_game.screen)

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
    
    def Fonction_quand_on_clique(self):
        main_game.screen.blit(self.image_rupture,self.rect_rupture)
        

    def Amelioration(self):

        print("test")