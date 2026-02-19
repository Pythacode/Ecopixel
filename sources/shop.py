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
        self.image_arrosoir,self.rect_arrosoir = self.img(192*2,192*2,50/2,50/2,"arrosoir.png")
        self.image_engrais,self.rect_engrais = self.img(192,192,200,500000,"engrais.png")
        self.image_pot,self.rect_pot = self.img(192,192,500,500,"pot.png")
        self.image_ruche,self.rect_ruche = self.img(192,192,750,750,"ruche.png")
        self.button = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (95*2,175*2), 265, 192/2, self.Fonction_quand_on_clique,"Bowser_fart_gif")

        self.items = json.load(tilsetJsonFile)
        self.header = True
        self.previous_view = None

        
    def  update (self,event):
        main_game.screen.fill("#ffe75d")
        main_game.screen.blit(self.image_arrosoir,self.rect_arrosoir)
        main_game.screen.blit(self.image_engrais,self.rect_engrais)
        main_game.screen.blit(self.image_pot,self.rect_pot)
        main_game.screen.blit(self.image_ruche,self.rect_ruche)
        self.button.update(main_game.screen)

    def img(self,width,height,x,y,path):
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
        rect = image.get_rect()
        rect.center = (x, y)
        image = pygame.transform.scale(image, (width,height))
        return image, rect
    
    def Fonction_quand_on_clique(self):
        print("test")