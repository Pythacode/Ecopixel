# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import requests
import threading
from game import *
import pygame
from view import view
from game import main_game

class searchView() :
    def __init__(self):
        # Fonction appelée à la création de la vue
        pygame.init()
        self.font = pygame.font.Font(main_game.main_font_name, 24)
        self.url_font = pygame.font.Font(main_game.main_font_name, 15)
        self.text_font = pygame.font.Font(main_game.main_font_name, 18)

        self.onsearch = False
        self.searchFiniched = False
        self.exploit_result = {}

        width = main_game.screen.get_size()[0]
        self.search_zone = entry_text(
            main_game.screen,
            main_game.BLACK,
            (70, 20),
            (width - 80, 40),
            2,
            20,
            self.font
        )
        self.search_zone.active = True

    def search(self, query:str, max_result=10, lang="fr"):
        """
        Recherche `query` grace à l'API de search1API
        https://www.search1api.com/#features
        
        :param query: Chaine de caractère à rechercher
        :type query: str
        :param max_result: Nombre maximum de résultats attendus.
        :type max_result: int
        :param lang: Langue de la recherche
        :type lang: str
        """

        self.searchFiniched = False

        API_URL = "https://api.search1api.com/search"
        
        # Paramètre de la recherche
        data = {
            "query": query,
            "max_results": max_result,
            "crawl_results": 2,  
            "image": False,
            "language": lang
        }

        # Headers de la requete
        headers = {
            "Content-Type": "application/json" # Réponse attendus en JSON
        }

        # Réponse de la requete
        response = requests.post(
            API_URL,
            headers=headers,
            json=data
        )

        results = response.json().get('results')
        self.exploit_result = [{
                "title" : r.get('title', "Titre inconu"),
                "link" : r.get('link', "Lien inconu"),
                "snippet" : r.get('snippet'),
                "content" : r.get('content', r.get('snippet', 'Aucune description')).removeprefix("---\\ndescription: ")
            } for r in results] # Suprime les informations inutiles à notre usage
        
        self.onsearch = False
        self.searchFiniched = True

    def update(self, events) :
        # Fonction appelée à chaque frame pour géré l'affichage

        main_game.screen.fill((255, 201, 157))

        if self.searchFiniched :
            pos_y = 90 - main_game.scroll_y
            pos_x = 20
            gap = 4
            for result in self.exploit_result :
                titleText = self.font.render(result.get('title'), True, main_game.BLACK)
                urlText = self.url_font.render(result.get('link').removeprefix("https://").removesuffix('/').replace('/', ' > '), True, (142, 142, 142))

                main_game.screen.blit(titleText, (pos_x, pos_y))

                text_height = self.font.size(result.get('title'))[1]
                pos_y += text_height + gap

                main_game.screen.blit(urlText, (pos_x, pos_y))
                pos_y += text_height + gap

                max_width = main_game.screen.get_size()[0] - 2*pos_x
                text_height = blit_text(result.get('snippet'), (pos_x, pos_y), self.text_font, max_width, main_game.BLACK, main_game.screen)
                pos_y += text_height + gap

                text_height = self.text_font.size("A")[1]
                pos_y += text_height + gap + 5
                
        elif self.onsearch :
            search_text = self.font.render("Chargement...", True, main_game.BLACK)
            main_game.screen.blit(search_text, (30, 100))

        width = main_game.screen.get_size()[0]

        # Header
        pygame.draw.rect(main_game.screen, main_game.WHITE, (0, 0, width, 80), width=0)

        logo_image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "logo.png"]))
        scaled_image = pygame.transform.scale(logo_image, (40, 40))
        main_game.screen.blit(scaled_image, (20, 20))

        #(70, 20, width - 80, 40)        

        text = self.search_zone.update(events)

        if isinstance(text, str) :
            if text != "" :
                self.onsearch = True
                threading.Thread(target=self.search, args=(text,), daemon=True).start()