# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par                                                               #
#      - Titouan - https://github.com/Pythacode/                         #
#      - Lucas - https://github.com/GreGrenier                           #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

import pygame
from searchEngine import searchView
from menu import menuView

WIDTH, HEIGHT = 1280, 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

current_view = menuView
current_view.init()

text = "hj"

while running:

    events = pygame.event.get()

    # Écout des évenement
    for event in events:
        # Quand l'utilisateur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False

    # Gérer le rendu
    current_view.update(events, screen)

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()