# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
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
            },
        'settings' :
            {
                'key_move_right' : main_game.key_move_right,
                'key_move_left' : main_game.key_move_left,
                'key_plant' : main_game.key_plant,
            },
        'game' :
            {
                'wait_tree' : None if main_game.game_view.wait_tree == None else {
                    'x' : main_game.game_view.wait_tree.get('x'),
                    'y' : main_game.game_view.wait_tree.get('y'),
                    'type': main_game.game_view.wait_tree.get('type')
                    },
                'trees' : [{
                    'x' : t.x,
                    'y' : t.y,
                    'time_alive' : t.time_alive,
                    'type' : t.type,
                    'seedling': t.seedling,
                    'growned_up': t.growned_up,
                    'skin_index': t.skin_index
                    } for t in main_game.game_view.tree]
            }
    }

with open(os.sep.join([main_game.asset_doc, 'data_game.json']), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
pygame.quit()
