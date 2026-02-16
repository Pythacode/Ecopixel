# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import *
import os
from tree import Tree
from dataclasses import dataclass

@dataclass
class Shop():
    image = pygame.image.load(os.sep.join([main_game.asset_doc, 'image', 'game', 'shop.png']))
    rect = image.get_rect()
    x = 30
    y = 0

class gameView() :

    def QuitButton_Pressed(self):
        main_game.running = False
    
    def settingsButton_Pressed(self):
        main_game.change_view(main_game.settings_view)

    def ResumeButton_Pressed(self):
        self.pause = False


    def __init__(self):
        self.offset_x = 0
        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "ground.png"]))
        self.last_frame = 0
        self.header = True
        self.pause = False
        gamedata = main_game.data.get('game', {})
        self.trees = []
        for tree in gamedata.get('trees', []) :
            self.trees.append(Tree(tree.get('x'), tree.get('y'), tree.get('type'), tree.get('time_alive'), tree.get('seedling'), tree.get('growned_up'), tree.get('skin_index'), tree.get('max_alive')))
        self.wait_tree = gamedata.get('wait_tree', None)

        self.resumebutton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + -100), 48*4, 24*4, self.ResumeButton_Pressed, text="Resume")
        self.settingsButton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2), 48*4, 24*4, self.settingsButton_Pressed, text="Réglages")
        self.quitbutton = button(os.sep.join([main_game.asset_doc, "image", "button", "quit_button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100), 48*4, 24*4, self.QuitButton_Pressed, text="")

    def update(self, events) :
        main_game.screen.fill(main_game.WHITE)

        ground_rect = self.ground.get_rect()
        width, height = main_game.screen.get_size()

        # Draw ground
        x = - ground_rect[2]
        ground_offset = self.offset_x % ground_rect[2] # ground offset
        while x < width :
            ground_rect[0], ground_rect[1] = x + ground_offset, height - ground_rect[3]
            main_game.screen.blit(self.ground, ground_rect)
            x += ground_rect[2]

        # Plant Player
        if main_game.touch_pressed.get(main_game.key_plant, False) and not main_game.player.plant and main_game.player.sprout >= 1:
            x = main_game.player.x - (main_game.player.size[0] + 10 if main_game.player.orientation == "LEFT" else 10) - self.offset_x
            # Générer une liste de tous les arbres qui sont proche de l'endroit ou le joueur veut planter une pousse
            t = list(filter(lambda tree : abs(tree.x - x) < 100, self.trees))
            if len(t) == 0 :
                main_game.player.plant_act()
                self.wait_tree = {'x' : x, 'y' : 0, 'type' : 'oak'}
                main_game.player.sprout -= 1
            else :
                main_game.player.say('Trop proche :/', 2_000)

        # Move player
        if main_game.touch_pressed.get(main_game.key_move_left, False) and not main_game.player.plant:
            if main_game.player.x > 200 :
                main_game.player.move_left()
            else :
                self.offset_x += main_game.player.velocity * main_game.dt
        if main_game.touch_pressed.get(main_game.key_move_right, False) and not main_game.player.plant:
            if main_game.player.x < width - main_game.player.size[1] - 200 :
                main_game.player.move_right()
            else :
                self.offset_x -= main_game.player.velocity * main_game.dt
        
        # Open Pause Menu
        if main_game.touch_pressed.get(pygame.K_ESCAPE, False) and not self.pause:
            self.pause = True

        for tree in filter(lambda e : -e.rect[2] <= e.x + self.offset_x <= width, self.trees) :
            tree.draw(main_game.screen, height - ground_rect[3], self.offset_x)

        main_game.player.draw(main_game.screen, height - ground_rect[3])

        if self.pause:
            # Header Pause Menu
            self.H_width = main_game.screen.get_width() - (150 * 2)
            self.H_height = main_game.screen.get_height() - (50 * 2)
            PM_bg = pygame.Surface((self.H_width, self.H_height))
            position = (main_game.screen.get_width()/2, main_game.screen.get_height()/2)
            PM_bg.set_alpha(128)
            PM_bg.fill((0, 0, 0))
            PM_bg_rect = PM_bg.get_rect()
            PM_bg_rect.center = position
            main_game.screen.blit(PM_bg, PM_bg_rect)

            # Pause Buttons
            self.resumebutton.update(main_game.screen)
            self.settingsButton.update(main_game.screen)
            self.quitbutton.update(main_game.screen)

        for event in events :
            if event.type == pygame.KEYDOWN:
                if event.key == main_game.key_move_left:
                    main_game.player.orientation = "LEFT"
                    main_game.player.move = True
                if event.key == main_game.key_move_right:
                    main_game.player.orientation = "RIGHT"
                    main_game.player.move = True
            if event.type == pygame.KEYUP:
                if event.key == main_game.key_move_left or event.key == main_game.key_move_right:
                    main_game.player.move = False
                    main_game.player.change_skin()
