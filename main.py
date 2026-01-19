# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par                                                               #
#      - Titouan - https://github.com/Pythacode/                         #
#      - Lucas - https://github.com/GreGrenier                           #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
from game import main_game

running = True

while running:

    events = pygame.event.get()

    # Écout des évenement
    for event in events:
        # Quand l'utilisateur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False

    # Gérer le rendu
    main_game.current_view.update(events)

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()