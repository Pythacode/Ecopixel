# --------------------------- Search engine ---------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #                                                          #
# ---------------------------------------------------------------------- #

import requests
import threading
from game import *
import pygame
from view import view

class searchView() :
    def __init__(self):
        pass

    def search(self, query:str, max_result=10, lang="fr") -> list:
        """
        Recherche `query` grace à l'API de search1API
        https://www.search1api.com/#features
        
        :param query: Chaine de caractère à rechercher
        :type query: str
        :param max_result: Nombre maximum de résultats attendus.
        :type max_result: int
        :param lang: Langue de la recherche
        :type lang: str
        :return: Une liste de dictionnaires qui comportent les informations de chaques résultats
        :rtype: list
        """

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

        print('send')

        # Réponse de la requete
        response = requests.post(
            API_URL,
            headers=headers,
            json=data
        )

        results = response.json().get('results')
        self.exploit_result = [{
                "title" : r.get('title'),
                "link" : r.get('link'),
                "snippet" : r.get('snippet')
            } for r in results] # Suprime les informations inutiles à notre usage
        
        print(self.exploit_result)


    def init(self) :

        pygame.init()
        self.text = "_"
        self.font = pygame.font.Font("freesansbold.ttf", 24)

        self.onsearch = False
        self.exploit_result = {}

    def update(self, events) :

        width, height = main_game.screen.get_size() 

        # Header
        pygame.draw.rect(main_game.screen, main_game.WHITE, (0, 0, width, 80), width=0)

        # Zone de recherche
        search_zone = pygame.draw.rect(
            main_game.screen,
            main_game.BLACK,
            (20, 20, width - 40, 40),
            width=2,
            border_radius=20,
        )

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if search_zone.collidepoint(event.pos):
                    print("Dans la zone")
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
                    threading.Thread(target=self.search, args=('Coucou',), daemon=True).start()
                elif event.key == pygame.K_BACKSPACE:
                    self.text =  self.text[:-2]
                    self.text += "_"
                else:
                    self.text =  self.text[:-1]
                    self.text += event.unicode + "_"

        text_pygame = self.font.render(self.text, True, main_game.BLACK)
        main_game.screen.blit(text_pygame, (27, 27))

        if self.onsearch :
            text_pygame = self.font.render("Chargement", True, main_game.WHITE)
            main_game.screen.blit(text_pygame, (30, 27))
