# ------------------------------ Setting ------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant le menu des réglages.                                #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

from game import *
import pygame
from game import *

class settingView():

    def __init__(self) :

        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.logo = pygame.transform.scale(main_game.logo, (150, 150))
        self.logo_rect = self.logo.get_rect()
        self.edit_id = None
        self.header = False
        self.key_edit = []
        self.previous_view = None

    def update(self, events) :

        self.settings = [
            {
                'id' : 'key_move_right',
                'name' : 'Touche droite',
                'value' : pygame.key.name(main_game.key_move_right)
            },
            {
                'id' : 'key_move_left',
                'name' : 'Touche gauche',
                'value' : pygame.key.name(main_game.key_move_left)
            },
            {
                'id' : 'key_plant',
                'name' : 'Touche planter',
                'value' : pygame.key.name(main_game.key_plant)
            }
        ]

        screen_width, height = main_game.screen.get_size() 

        main_game.screen.fill((255, 201, 157))

        self.logo_rect[0] = screen_width / 2 - self.logo_rect[2] / 2
        self.logo_rect[1] = main_game.scroll_y
        main_game.screen.blit(self.logo, self.logo_rect)

        pos_y = 200

        for setting in self.settings :
            # Titre
            title_text = self.font.render(setting.get('name'), True, main_game.BLACK)

            main_game.screen.blit(title_text, (10, pos_y + main_game.scroll_y))

            # Key
            text = "Appuyer sur une touche" if self.edit_id == setting.get('id') else setting.get('value')
            
            width, height = self.font.size(text)
            x = screen_width - 10 - width
            key_text = self.font.render(text, True, main_game.BLACK)

            main_game.screen.blit(key_text, (x, pos_y + main_game.scroll_y))

            self.key_edit.append({
                'rect' : pygame.Rect(x, pos_y + main_game.scroll_y, width, height),
                'id' : setting.get('id')
            })

            pos_y += self.font.size(setting.get('name'))[1] + 20

        back_rect = main_game.back.get_rect()
        back_rect[0], back_rect[1] = 10, 10
        main_game.screen.blit(main_game.back, back_rect)

        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if back_rect.collidepoint(event.pos) :
                    main_game.change_view(self.previous_view)
                if self.edit_id == None :
                    for i in self.key_edit :
                        if i.get('rect').collidepoint(event.pos) :
                            self.edit_id = i.get('id')
            
            elif event.type == pygame.KEYDOWN and self.edit_id is not None :
                    setattr(main_game, self.edit_id, event.key)
                    self.edit_id = None
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                main_game.change_view(self.previous_view)
