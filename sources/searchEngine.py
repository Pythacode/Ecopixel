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
import re

CLEAN_HTML_BALISE_REGEX = '<.*?>'

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
            'black',
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

        self.min_scroll_y = self.max_scroll_y = 0

    def search(self, query:str, lang="fr"):
        """
        Recherche `query` grace à l'API de wikipedia
        
        :param query: Chaine de caractère à rechercher
        :type query: str
        :param lang: Langue de la recherche
        :type lang: str
        """

        self.searchFiniched = False

        API_URL = f"https://fr.wikipedia.org/w/api.php"
        
        # Paramètre de la recherche
        data = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "origin": "*"
        }

        # Headers de la requete
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Réponse de la requete
        try :
            response = requests.get(API_URL, params=data, headers=headers)
            data = response.json()

            if response.status_code != 200 :
                self.exploit_result = {
                    "result" : "error",
                    "type" : 'unknow',
                    "error" : "Coded'érreur : {response.status_code}"
                }
                
            else :
                self.exploit_result = {
                        "result" : "succes",
                        "data" : [
                                {
                                    "title" : resultat.get('title', "Titre inconu"),
                                    "link" : f"https://fr.wikipedia.org/wiki/{resultat.get('title', "Lien inconu")}",
                                    "snippet" : re.sub(CLEAN_HTML_BALISE_REGEX, '',resultat.get('snippet'))
                                } for resultat in data["query"]["search"]
                            ]
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
        except Exception as e :
            self.exploit_result = {
                    "result" : "error",
                    "type" : 'unknow',
                    "error" : e
                }


        
        self.onsearch = False
        self.searchFiniched = True

    def update(self, events) :
        # Fonction appelée à chaque frame pour gérer l'affichage

        main_game.screen.fill((255, 201, 157))

        if self.searchFiniched :
            pos_y = 140 - main_game.scroll_y
            pos_x = 20
            gap = 4
            self.results_rect = []
            if self.exploit_result.get('result') == 'succes' :
                main_game.player.sprout += 1
                for result in self.exploit_result.get('data') :

                    start_y = pos_y

                    titleText = self.font.render(result.get('title'), True, 'black')
                    urlText = self.url_font.render(result.get('link').removeprefix("https://").removesuffix('/').replace('/', ' > '), True, (142, 142, 142))

                    main_game.screen.blit(titleText, (pos_x, pos_y))

                    width, text_height = self.font.size(result.get('title'))
                    pos_y += text_height + gap

                    main_game.screen.blit(urlText, (pos_x, pos_y))
                    pos_y += text_height + gap

                    max_width = main_game.screen.get_size()[0] - 2*pos_x
                    text_height = blit_text(result.get('snippet'), (pos_x, pos_y), self.text_font, max_width, 'black', main_game.screen)
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
                screen_width, screen_height = main_game.screen.get_size() 
                self.min_scroll_y = pos_y - screen_height
                self.min_scroll_y = 0 if self.min_scroll_y < 0 else self.min_scroll_y
            elif self.exploit_result.get('result') == 'error' :
                self.min_scroll_y = 0
                if self.exploit_result.get('type') == 'ConnectionError' :
                    search_text = self.font.render("Pas de connection internet.", True, 'black')
                    main_game.screen.blit(search_text, (30, 140))
                elif self.exploit_result.get('type') == 'ReadTimeout' :
                    search_text = self.font.render("Délais d'attente dépassé. Vérifier votre connection et votre pare-feux.", True, 'black')
                    main_game.screen.blit(search_text, (30, 140))
                elif self.exploit_result.get('type') == 'unknow' :
                    print(self.exploit_result["error"])
                    search_text = self.font.render("Une erreur inconnue s'est produite.", True, 'black')
                    main_game.screen.blit(search_text, (30, 140))
            else :
                self.min_scroll_y = 0
                
        elif self.onsearch :
            now = pygame.time.get_ticks()
            if now - self.last_change > 500 :
                self.last_change = now
                self.message_index += 1
                if self.message_index >= len(self.search_message) :
                    self.message_index = 0
            search_text = self.font.render(self.search_message[self.message_index], True, 'black')
            main_game.screen.blit(search_text, (30, 140))

        width = main_game.screen.get_size()[0]

        # Header
        pygame.draw.rect(main_game.screen, 'white', (0, 40, width, 85), width=0)

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(event.pos) :
                    main_game.change_view(self.previous_view)
                    break
                for i in self.results_rect :
                    if i.get('rect').collidepoint(event.pos) :
                        webbrowser.open(i.get('link'))
            elif event.type == pygame.KEYDOWN and event.key == main_game.key_back :
                main_game.change_view(self.previous_view)
