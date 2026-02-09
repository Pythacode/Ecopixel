# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
import json
from game import *

last_frame = 0

while main_game.running:

    events = pygame.event.get()

    # Écout des évenement
    for event in events:
        # Quand l'utilisateur ferme la fenetre
        if event.type == pygame.QUIT:
            main_game.running = False
        elif event.type == pygame.MOUSEWHEEL:
            main_game.scroll_y -= event.y * 10
            main_game.scroll_x -= event.x * 10
        elif event.type == pygame.KEYDOWN :
            main_game.touch_pressed[event.key] = True
        elif event.type == pygame.KEYUP :
            main_game.touch_pressed[event.key] = False

    # Calculate delta time
    now = pygame.time.get_ticks()
    main_game.dt =  (now - last_frame)
    last_frame = now

    # Gérer le rendu
    main_game.current_view.update(events)
    if main_game.current_view.header : # Si la vue nécésite l'affichage du header'
        draw_header()

    # Actualiser l'écran
    pygame.display.flip()

# Sauvegarde des données

data = {
        'player' : 
            {
                'x' : main_game.player.x,
                'y' : main_game.player.y,
                'money' : main_game.player.money,
                'sprout' : main_game.player.sprout,
                'orientation' : main_game.player.orientation,
                'skin_index' : main_game.player.skin_index,
                'plant' : main_game.player.plant
            }
        ,
        'settings' :
            {
                'key_move_right' : main_game.key_move_right,
                'key_move_left' : main_game.key_move_left,
                'key_plant' : main_game.key_plant,
            }
        
    }

with open(os.sep.join([main_game.asset_doc, 'data_game.json']), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
pygame.quit()
