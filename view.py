# -------------------------------- View -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant une classe pour créer une vue du jeux                #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License :                                                              #
# ---------------------------------------------------------------------- #

class view() :
    def __init__(self, event:function, render:function) -> None:
        """
        Crée une vue pour le jeux
        
        :param event: Une fonction qui sert à gérer les événements pygame quand la vue est active. Elle doit attendre un argument \: l’événement à gérer.
        :type event: function
        :param render: Une fonction qui sert à gérer le rendu de la vue. Elle doit attendre aucun argument.
        :type render: function
        """
        self.event = event # Fonction qui sera appelée pour gérer les évènements pygame
        self.render = render # Fonction qui sera appelée pour gérer les évènements pygame

