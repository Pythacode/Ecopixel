# -------------------------------- Game -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant toute les variable globals du jeux                   #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License :                                                              #
# ---------------------------------------------------------------------- #

from typing import Callable

class view() :
    def __init__(self, update:Callable) -> None:
        """
        Crée une vue pour le jeux
        
        :param update: Une fonction qui sert à gérer actualiser la vue.. Elle doit attendre deux argument, la liste d'évènement et un objet surface qui correspond à l'écran.
        :type update: Callable
        """
        self.update = update # Fonction qui sera appelée pour gérer les évènements pygame


WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
