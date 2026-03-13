# -------------------------------- tuto -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant le tuto du jeux                                      #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import main_game
import pygame

class Tuto() :
    def __init__(self):
        self.step = ["present", "search", "plant", "recolte", "buy"]
        self.advencement = main_game.data.get('game', {}).get('tuto_advancement', 0)
        self.messages = {
            "present" : f"Bienvenu sur Écopixel.\nNous allons te guider pas à pas pour que tu aprenne à jouer. Si tu est bloqué·e, appuie sur la touche {pygame.key.name(main_game.key_help)}.",
            "search" : f"Vas devant ta maison et appuie sur {pygame.key.name(main_game.key_action)}, ensuite, fait des recherches pour gagner des pousses ",
            "plant" : f"Vas sur un espace vide et appuie sur {pygame.key.name(main_game.key_action)} pour planter un arbre",
            "plant" : f"Attend que des fruit tombe d'un arbre, puis récupère les avec {pygame.key.name(main_game.key_action)}",
            "plant" : f"Vas devant le shop et appuie sur {pygame.key.name(main_game.key_action)}, vend tes fruits et achete de l'engrais"
        }

    def get_message(self) :
        return self.messages.get(self.step[self.advencement], "")
        
    def get_advancement(self) -> str :
        return self.step[self.advencement]

    def help(self) :
        main_game.player.say(self.get_message(), 2000)
    
    def next(self):
        self.advencement += 1
        self.help()