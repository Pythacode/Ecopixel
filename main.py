# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
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
        if event.type == pygame.MOUSEWHEEL:
            main_game.scroll_y -= event.y * 10
            main_game.scroll_x -= event.x * 10


    # Gérer le rendu
    main_game.current_view.update(events)

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()