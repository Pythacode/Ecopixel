# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
from game import main_game

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


    # Gérer le rendu
    main_game.current_view.update(events)

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()