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

# Boucle principal du jeu
while main_game.running:

    events = pygame.event.get()

    # Écout des évenement
    for event in events:
        # Quand l'utilisateur ferme la fenetre
        if event.type == pygame.QUIT:
            main_game.running = False
        
        # Losrque l'utilisateur scrolle
        elif event.type == pygame.MOUSEWHEEL:
            main_game.scroll_y -= event.y * 10
            main_game.scroll_x -= event.x * 10

        # lorsqu'il appuie sur une touche
        elif event.type == pygame.KEYDOWN :
            main_game.touch_pressed[event.key] = True # Met `TRUE` à la clé `event.key`
            # Si la touche est la touche de sauvegarde
            if event.key == main_game.key_save : # On lance la sauvegarde
                main_game.save()

        # Lorsqu'il relache la touche
        elif event.type == pygame.KEYUP :
            main_game.touch_pressed[event.key] = False # Met `TRUE` à la clé `event.key`

    # Calculate delta time
    now = pygame.time.get_ticks()
    main_game.dt =  (now - last_frame)
    last_frame = now

    # Gérer le rendu
    main_game.current_view.update(events)
    if main_game.current_view.header : # Si la vue nécésite l'affichage du header
        draw_header()

    # Actualiser l'écran
    pygame.display.flip()

# Sauvegarde des données
main_game.save()

pygame.quit()
