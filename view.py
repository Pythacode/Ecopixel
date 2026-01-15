# -------------------------------- View -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant une classe pour créer une vue du jeux                #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License :                                                              #
# ---------------------------------------------------------------------- #

class view() :
    def __init__(self, event:function, render:function):
        self.event = event # Fonction qui seras apeller pour gerer les évènements pygames
        self.render = render # Fonction qui seras apeller pour faire le rendus du jeux