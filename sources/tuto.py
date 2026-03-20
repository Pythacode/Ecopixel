# -------------------------------- tuto -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant le tuto du jeux                                      #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import main_game
import pygame

class Tuto() :
    def __init__(self, advencement):
        
        self.steps = ["present", "search", "plant", "recolte", "buy", "Finish"]
        self.advencement = advencement
        self.messages = {
            "present" : f"Bienvenu sur Écopixel.\nNous allons te guider pas à pas pour que tu aprenne à jouer. Si tu est bloqué·e, appuie sur la touche {pygame.key.name(main_game.key_help)}.",
            "search" : f"Vas devant ta maison et appuie sur {pygame.key.name(main_game.key_action)}, ensuite, fait des recherches pour gagner des pousses ",
            "plant" : f"Vas sur un espace vide et appuie sur {pygame.key.name(main_game.key_action)} pour planter un arbre",
            "recolte" : f"Attend que des fruit tombe d'un arbre, puis récolte le en passant dessus.",
            "buy" : f"Vas devant le shop et appuie sur {pygame.key.name(main_game.key_action)}, vend tes fruits et achete de l'engrais",
            "Finish" : f"Le tuto est fini, la suite du jeu arrive."
        }

    def get_message(self) -> str :
        return self.messages.get(self.steps[self.advencement], "")
        
    def get_advancement(self) -> str :
        return self.steps[self.advencement]

    def help(self) -> None:
        main_game.player.say(self.get_message(), 2000)
    
    def next(self, source) -> None:
        """
        Passed to next step.

        :param source: Source de la demande de changement d'étape.
        :type source: None
        """
        if source == self.steps[self.advencement] :
            self.advencement += 1
            self.help()
