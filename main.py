# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par                                                               #
#      - Titouan - https://github.com/Pythacode/                         #
#      - Lucas - https://github.com/GreGrenier                           #
# License :                                                              #
# ---------------------------------------------------------------------- #

import pygame
from searchEngine import searchEngine

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

current_view = searchEngine

while running:

    # Écout des évenement
    for event in pygame.event.get():
        # Quand l'utilisateur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
        current_view.event(event)

    # Gérer le rendu
    current_view.render()

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()