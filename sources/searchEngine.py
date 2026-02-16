# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import requests
import threading
from game import *
import pygame
import webbrowser

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
            (70, 60),
            (width - 80, 40),
            2,
            20,
            self.font
        )
        self.search_zone.active = True
        self.header = True
        self.previous_view = None

        self.results_rect = []
        self.search_message = ['Chargement', 'Chargement.', 'Chargement..', 'Chargement...']
        self.message_index = 0
        self.last_change = pygame.time.get_ticks()

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
        try :
            response = requests.post(
                API_URL,
                headers=headers,
                json=data
            )
            results = response.json().get('results')
            self.exploit_result = {
                    "result" : "succes",
                    "data" : [{
                        "title" : r.get('title', "Titre inconu"),
                        "link" : r.get('link', "Lien inconu"),
                        "snippet" : r.get('snippet'),
                        "content" : r.get('content', r.get('snippet', 'Aucune description')).removeprefix("---\\ndescription: ")
                        } for r in results]
            } # Suprime les informations inutiles à notre usage
        except requests.exceptions.ReadTimeout :
            self.exploit_result = {
                    "result" : "error",
                    "type" : 'ReadTimeout'
                }
        except requests.exceptions.ConnectionError :
            self.exploit_result = {
                    "result" : "error",
                    "type" : 'ConnectionError'
                }
        except :
            self.exploit_result = {
                    "result" : "error",
                    "type" : 'unknow'
                }


        
        self.onsearch = False
        self.searchFiniched = True

    def update(self, events) :
        # Fonction appelée à chaque frame pour géré l'affichage

        main_game.screen.fill((255, 201, 157))

        if self.searchFiniched :
            pos_y = 140 - main_game.scroll_y
            pos_x = 20
            gap = 4
            self.results_rect = []
            if self.exploit_result.get('result') == 'succes' :
                for result in self.exploit_result.get('data') :

                    start_y = pos_y

                    titleText = self.font.render(result.get('title'), True, main_game.BLACK)
                    urlText = self.url_font.render(result.get('link').removeprefix("https://").removesuffix('/').replace('/', ' > '), True, (142, 142, 142))

                    main_game.screen.blit(titleText, (pos_x, pos_y))

                    width, text_height = self.font.size(result.get('title'))
                    pos_y += text_height + gap

                    main_game.screen.blit(urlText, (pos_x, pos_y))
                    pos_y += text_height + gap

                    max_width = main_game.screen.get_size()[0] - 2*pos_x
                    text_height = blit_text(result.get('snippet'), (pos_x, pos_y), self.text_font, max_width, main_game.BLACK, main_game.screen)
                    pos_y += text_height + gap

                    if max_width > width :
                        width = max_width

                    text_width, text_height = self.text_font.size("A")
                    pos_y += text_height + gap + 5

                    if text_width > width :
                        width = text_width

                    self.results_rect.append({
                        'rect' : pygame.Rect(pos_x, start_y, width, (pos_y - 5 - gap)-start_y),
                        'link' : result.get('link')
                    })
            elif self.exploit_result.get('result') == 'error' :
                if self.exploit_result.get('type') == 'ConnectionError' :
                    search_text = self.font.render("Pas de connection internet", True, main_game.BLACK)
                    main_game.screen.blit(search_text, (30, 140))
                elif self.exploit_result.get('type') == 'ReadTimeout' :
                    search_text = self.font.render("Délais d'attente dépassé. Verifier votre connection et votre par-feux", True, main_game.BLACK)
                    main_game.screen.blit(search_text, (30, 140))
                elif self.exploit_result.get('type') == 'unknow' :
                    search_text = self.font.render("Une érreur inconue s'est produite", True, main_game.BLACK)
                    main_game.screen.blit(search_text, (30, 140))
                
        elif self.onsearch :
            now = pygame.time.get_ticks()
            if now - self.last_change > 500 :
                self.last_change = now
                self.message_index += 1
                if self.message_index >= len(self.search_message) :
                    self.message_index = 0
            search_text = self.font.render(self.search_message[self.message_index], True, main_game.BLACK)
            main_game.screen.blit(search_text, (30, 140))

        width = main_game.screen.get_size()[0]

        # Header
        pygame.draw.rect(main_game.screen, main_game.WHITE, (0, 40, width, 85), width=0)

        back_rect = main_game.back.get_rect()
        back_rect[0], back_rect[1] = 20, 70
        main_game.screen.blit(main_game.back, back_rect)

        #(70, 20, width - 80, 40)        

        text = self.search_zone.update(events)

        if isinstance(text, str) :
            if text != "" :
                self.onsearch = True
                threading.Thread(target=self.search, args=(text,), daemon=True).start()

        mouse_pos = pygame.mouse.get_pos()
        cursor = (pygame.cursors.Cursor(),)
        for i in self.results_rect :
            if i.get('rect').collidepoint(mouse_pos) :
                cursor = pygame.cursors.tri_left
                break
        pygame.mouse.set_cursor(*cursor)

        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if back_rect.collidepoint(event.pos) :
                    main_game.change_view(self.previous_view)
                    break
                for i in self.results_rect :
                    if i.get('rect').collidepoint(event.pos) :
                        webbrowser.open(i.get('link'))
                        main_game.player.sprout += 1
            elif event.type == pygame.K_ESCAPE :
                main_game.change_view(self.previous_view)
