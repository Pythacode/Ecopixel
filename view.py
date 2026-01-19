# -------------------------------- Game -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant la classe pour les vues du jeux                      #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #
 
from typing import Callable

class view() :
    def __init__(self, init:Callable, update:Callable) -> None:
        """
        Crée une vue pour le jeux
        
        :param update: Une fonction qui sert à gérer actualiser la vue. Elle doit attendre deux argument, la liste d'évènement et un objet surface qui correspond à l'écran.
        :type update: Callable
        :param init: Une fonction qui sert à initialiser la vue.
        :type init: Callable
        """
        self.init = init
        self.update = update