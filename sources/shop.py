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
        self.image_arrosoir,self.rect_arrosoir = self.img(288,288, (200, 150),"arrosoir.png")
        self.image_engrais,self.rect_engrais = self.img(192,192,(450,150),"engrais.png")
        self.image_pot,self.rect_pot = self.img(192,192,(700,150),"pot.png")
        self.image_ruche,self.rect_ruche = self.img(192,192,(950,150),"ruche.png")
        self.arrosoir_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (180,300), 192, 192/2, self.Fonction_quand_on_clique,"Arrosoir")
        self.engrais_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (450,300), 192, 192/2, self.Fonction_quand_on_clique,"Engrais")
        self.pot_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (700,300), 192, 192/2, self.Fonction_quand_on_clique,"Pot")
        self.ruche_btn = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (950,300), 192, 192/2, self.Fonction_quand_on_clique,"Ruche")


        self.items = json.load(tilsetJsonFile)
        self.header = True
        self.previous_view = None

        
    def  update (self,event):
        main_game.screen.fill("#ffe75d")
        main_game.screen.blit(self.image_arrosoir,self.rect_arrosoir)
        main_game.screen.blit(self.image_engrais,self.rect_engrais)
        main_game.screen.blit(self.image_pot,self.rect_pot)
        main_game.screen.blit(self.image_ruche,self.rect_ruche)
        self.arrosoir_btn.update(main_game.screen)
        self.engrais_btn.update(main_game.screen)
        self.pot_btn.update(main_game.screen)
        self.ruche_btn.update(main_game.screen)

    def img(self,width,height,position,path):
        """
        Données pour la fonction img:

        :param width: Largeur de l'image en int
        :param height: Hauteur de l'image en int
        :param x: Position horizontale de l'image en int
        :param y: Position verticale de l'image en int
        :param path: Chemin dans les fichier de l'image à afficher en str
        """
        # Résultat : Affiche une image sur la fenêtre

        image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "item", path]))
        image = pygame.transform.scale(image, (width,height))
        rect = image.get_rect()
        rect.center = position
        return image, rect
    
    def Fonction_quand_on_clique(self):
        print("test")