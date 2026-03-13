# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import *
import os
from tree import Tree
from house import House
from shop_place import Shop_place

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
        self.fruits = []

        house_data = gamedata.get('house', {})
        self.h = House(lvl=house_data.get('lvl', 1))
        self.s = Shop_place(-500)
        self.eimg = pygame.image.load(os.sep.join([main_game.asset_doc,"image","button","Ebtn.png"]))

        self.resumebutton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + -100), 48*4, 24*4, self.ResumeButton_Pressed, text="Resume")
        self.settingsButton = button(os.sep.join([main_game.asset_doc, "image", "button", "settings_button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "settings_button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "settings_button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2), 48*4, 24*4, self.settingsButton_Pressed)
        self.quitbutton = button(os.sep.join([main_game.asset_doc, "image", "button", "quit_button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100), 48*4, 24*4, self.QuitButton_Pressed, text="")
        self.tutoButton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100), 48*4, 24*4, main_game.tuto.next, text="Jouer")

    def update(self, events) :
        main_game.screen.fill('white')

        ground_rect = self.ground.get_rect()
        width, height = main_game.screen.get_size()

        # Draw ground
        x = - ground_rect[2]
        ground_offset = self.offset_x % ground_rect[2] # ground offset
        while x < width :
            ground_rect[0], ground_rect[1] = x + ground_offset, height - ground_rect[3]
            main_game.screen.blit(self.ground, ground_rect)
            x += ground_rect[2]       

        self.h.draw(main_game.screen, height - ground_rect[3], self.offset_x)
        self.s.draw(main_game.screen, height - ground_rect[3], self.offset_x)

        for tree in self.trees :
            tree.draw(main_game.screen, height - ground_rect[3], self.offset_x)
        for fruit in self.fruits :
            fruit.draw(main_game.screen, height - ground_rect[3], self.offset_x)

        main_game.player.draw(main_game.screen, height - ground_rect[3])

        # Open Pause Menu
        if (main_game.touch_pressed.get(main_game.key_pause, False) or main_game.touch_pressed.get(main_game.key_back, False)) and not self.pause:
            self.pause = True

        if main_game.tuto.get_advancement() == "present" : # Tuto Menu
            self.H_width = main_game.screen.get_width() - (150 * 2)
            self.H_height = main_game.screen.get_height() - (50 * 2)
            PM_bg = pygame.Surface((self.H_width, self.H_height))
            position = (main_game.screen.get_width()/2, main_game.screen.get_height()/2)
            PM_bg.set_alpha(128)
            PM_bg.fill((0, 0, 0))
            PM_bg_rect = PM_bg.get_rect()
            PM_bg_rect.center = position
            main_game.screen.blit(PM_bg, PM_bg_rect)

            font = pygame.font.Font(main_game.main_font_name, 24) # Charge la police
            ws, hs = main_game.screen.get_size() # Obtient la taille de l'écran

            h, w = size_text(main_game.tuto.get_message(), font, ws/2)

            blit_text(main_game.tuto.get_message(), (ws/2 - w/2, hs/2 - h/2), font, ws/2, "white", main_game.screen)

            self.tutoButton.update(main_game.screen, (main_game.screen.get_width()/2, main_game.screen.get_height()/2+h+50))
            return
            
        elif self.pause:
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
            self.resumebutton.update(main_game.screen, (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + -100))
            self.settingsButton.update(main_game.screen, (main_game.screen.get_width()/2, main_game.screen.get_height()/2))
            self.quitbutton.update(main_game.screen, (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100)) 
            return

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

        x = main_game.player.x - self.offset_x

        # Display action touche
        # If distance between center of house & shop < half of his :
        #     display_action_touch
        if (abs((self.h.x + self.h.size[0]/2) - x) < self.h.size[0]/2) or (abs((self.s.x + self.s.size[0]/2) - x) < self.s.size[0]/2):
            img = pygame.transform.scale(self.eimg, (72, 72))
            rect = img.get_rect()
            rect.center = (main_game.player.x + 60, height - ground_rect[3] - 250)
            main_game.screen.blit(img, rect)

        if main_game.touch_pressed.get(main_game.key_action, False) :
            
            # Search
            if abs((self.h.x + self.h.size[0]/2) - x) < self.h.size[0]/2:
                img = pygame.transform.scale(self.eimg, (72, 72))
                rect = img.get_rect()
                rect.center = (main_game.player.x + 60, height - ground_rect[3] - 250)
                main_game.screen.blit(img, rect)
                main_game.change_view(main_game.search_view)

            # Shop
            if abs((self.s.x + self.s.size[0]/2) - x) < self.s.size[0]/2:
                img = pygame.transform.scale(self.eimg, (72, 72))
                rect = img.get_rect()
                rect.center = (main_game.player.x + 60, height - ground_rect[3] - 250)
                main_game.screen.blit(img, rect)
                main_game.change_view(main_game.shop_view)

            # Plant
            elif not main_game.player.plant and main_game.player.sprout >= 1 and not abs(self.h.x + 200 - x) < 100:
                x = main_game.player.x - (main_game.player.size[0] + 10 if main_game.player.orientation == "LEFT" else 10) - self.offset_x
                # Générer une liste de tous les arbres qui sont proche de l'endroit où le joueur veut planter une pousse
                t = list(filter(lambda tree : abs(tree.x - x) < 100, self.trees))
                if len(t) == 0 : # Verrifier si elle est vide
                    main_game.player.plant_act()
                    self.wait_tree = {'x' : x, 'y' : 0, 'type' : 'oak'}
                    main_game.player.sprout -= 1
                else :
                    main_game.player.say('Trop proche :/', 2_000)

        for event in events :
            if event.type == pygame.KEYDOWN:
                if event.key == main_game.key_move_left:
                    main_game.player.orientation = "LEFT"
                    main_game.player.move = True
                if event.key == main_game.key_move_right:
                    main_game.player.orientation = "RIGHT"
                    main_game.player.move = True
                if event.key == main_game.key_help:
                    main_game.tuto.help()
            if event.type == pygame.KEYUP:
                if event.key == main_game.key_move_left or event.key == main_game.key_move_right:
                    main_game.player.move = False
                    main_game.player.change_skin()
