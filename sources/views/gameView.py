# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par                                                               #
#              - Titouan - https://github.com/Pythacode/                 #
#              - Lucas - https://github.com/GreGrenier/                  #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import *
import os
from sprites.tree import Tree
from buildings.house import House
from buildings.shop_place import Shop_place
from sprites.cloud import Cloud
from sprites.moutain import Mountain
from sprites.player import Player
from buildings.place_block import Decoration, decoration_type, list_decoration_type

class gameView() :

    def QuitButton_Pressed(self):
        main_game.running = False
    
    def settingsButton_Pressed(self):
        main_game.change_view(main_game.settings_view)

    def ResumeButton_Pressed(self):
        self.pause = False


    def __init__(self, gamedata=None, playerdata=None, players=None):
        """
        init function
        """

        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "ground.png"]))
        self.last_frame = 0
        self.header = True
        self.pause = False

        if gamedata is None :
            if os.path.exists(os.sep.join([main_game.jsonPath, "sauv_game.json"])) and not main_game.connect :
                gamedata = open(os.sep.join([main_game.jsonPath, "sauv_game.json"]), 'r')
                gamedata = json.load(gamedata).get('game', {})
            else :
                gamedata = {}

        self.trees = []
        for tree in gamedata.get('trees', []) :
            self.trees.append(Tree(tree.get('x'), tree.get('y'), tree.get('type'), tree.get('fertilized'), tree.get('time_alive'), tree.get('seedling'), tree.get('growned_up'), tree.get('skin_index'), tree.get('max_alive')))
        self.wait_tree = gamedata.get('wait_tree', None)
        self.fruits = []

        house_data = gamedata.get('house', {})
        self.h = House(lvl=house_data.get('lvl', 1))
        self.s = Shop_place(-500)
        self.eimg = pygame.image.load(os.sep.join([main_game.asset_doc,"image","button","Ebtn.png"]))

        self.clouds = [Cloud() for i in range(1000)]
        self.mountains = [Mountain() for i in range(250)]

        self.decorations = []
        self.decor_type = ""
        self.actual_decoration = None

        self.resumebutton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + -100), 48*4, 24*4, self.ResumeButton_Pressed, text="Resume")
        self.settingsButton = button(os.sep.join([main_game.asset_doc, "image", "button", "settings_button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "settings_button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "settings_button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2), 48*4, 24*4, self.settingsButton_Pressed)
        self.quitbutton = button(os.sep.join([main_game.asset_doc, "image", "button", "quit_button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "quit_button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100), 48*4, 24*4, self.QuitButton_Pressed, text="")
        self.tutoButton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (main_game.screen.get_width()/2, main_game.screen.get_height()/2 + 100), 48*4, 24*4, lambda : main_game.tuto.next("present"), text="Jouer")

        self.cloud1 = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "background", "cloud1.png"]))

        center = main_game.screen.get_size()[0] / 2
        main_game.player = Player(center, playerdata)
        self.offset_x = center - main_game.player.x

        if main_game.connect :
            self.players = {}
            for p in players :
                self.add_player(p)

        self.last_actualisation = pygame.time.get_ticks()

    def add_player(self, p) :
        self.players[p['username']] = Player(main_game.screen.get_size()[0] / 2, playerdata=p, pnj=True)

    def draw_deco_case(self, img, size:tuple, pos:tuple) :
        
        selected_case = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "deco_selector", "case.png"]))
        selected_case = pygame.transform.scale(selected_case, size)

        rect = selected_case.get_rect()
        rect.center = pos
        main_game.screen.blit(selected_case, rect)

        selected_deco = pygame.transform.scale(img, (size[0] - 20, size[1] - 20))

        rect = selected_deco.get_rect()
        rect.center = pos
        main_game.screen.blit(selected_deco, rect)

    def update(self, events) :
        """
        Update function
        """
        main_game.screen.fill('blue')

        ground_rect = self.ground.get_rect()
        width, height = main_game.screen.get_size()

        # Draw ground
        x = - ground_rect[2]
        ground_offset = self.offset_x % ground_rect[2] # ground offset
        while x < width :
            ground_rect[0], ground_rect[1] = x + ground_offset, height - ground_rect[3]
            main_game.screen.blit(self.ground, ground_rect)
            x += ground_rect[2]       

        ground_altitude = height - ground_rect[3]

        for cloud in self.clouds:
            cloud.draw(main_game.screen, ground_altitude, self.offset_x)
        for mountain in self.mountains:
            mountain.draw(main_game.screen, ground_altitude, self.offset_x)

        self.h.draw(main_game.screen, ground_altitude, self.offset_x)
        self.s.draw(main_game.screen, ground_altitude, self.offset_x)

        for tree in self.trees :
            tree.draw(main_game.screen, ground_altitude, self.offset_x)
        for fruit in self.fruits :
            fruit.draw(main_game.screen, ground_altitude, self.offset_x)
        main_game.player.draw(main_game.screen, ground_altitude, self.offset_x)

        for decor in self.decorations:
            decor.draw(main_game.screen, ground_altitude, self.offset_x)
        if self.actual_decoration :
            self.actual_decoration.draw(main_game.screen, ground_altitude, self.offset_x)
            selector_arrow = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "deco_selector", "arrow.png"]))
            selector_arrow = pygame.transform.scale(selector_arrow, (62, 62))

            rect = selector_arrow.get_rect()
            rect.center = width / 2, ground_altitude - 100
            main_game.screen.blit(selector_arrow, rect)
            self.draw_deco_case(self.actual_decoration.actual_skin, (62, 62), (width / 2, ground_altitude - 30))

            font = pygame.font.Font(main_game.main_font_name, 24)
            
            price = font.render(f"{decoration_type[self.actual_decoration.type]["price"]:,}".replace(',', ' '), 0, 'black')
            word_width = price.get_size()[0]
            rect = price.get_rect()
            rect.center = width/2 - word_width/2, ground_altitude + 20
            main_game.screen.blit(price, rect)

            image = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "icon", "coin.png"]))
            scaled_image = pygame.transform.scale(image, (20, 20))
            rect = scaled_image.get_rect()
            rect.center = width/2 + word_width/2, ground_altitude + 20
            main_game.screen.blit(scaled_image, rect)

            select_index = list_decoration_type.index(self.actual_decoration.type)

            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index-3)%(len(list_decoration_type))])['img'], (32, 32), ((width / 2) - 155, ground_altitude - 30))
            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index-1)%(len(list_decoration_type))])['img'], (52, 52), ((width / 2) - 70, ground_altitude - 30))
            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index-2)%(len(list_decoration_type))])['img'], (45, 45), ((width / 2) - 125, ground_altitude - 30))

            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index+3)%(len(list_decoration_type))])['img'], (32, 32), ((width / 2) + 155, ground_altitude - 30))
            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index+1)%(len(list_decoration_type))])['img'], (52, 52), ((width / 2) + 70, ground_altitude - 30))
            self.draw_deco_case(decoration_type.get(list_decoration_type[(select_index+2)%(len(list_decoration_type))])['img'], (45, 45), ((width / 2) + 125, ground_altitude - 30))

        if main_game.connect :
            for p in self.players.values() :
                assert p.username != main_game.player.username, "Heu... Bro ?"
                if p.username == "Nath" : pass
                p.draw(main_game.screen, height-ground_rect[3], self.offset_x)
                if p.move :
                    if p.orientation == "LEFT" :
                        p.move_left()
                    elif p.orientation == "RIGHT" :
                        p.move_right()

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
            main_game.player.move_left()
        if main_game.touch_pressed.get(main_game.key_move_right, False) and not main_game.player.plant:
            main_game.player.move_right()

        x = main_game.player.get_relativ_x(self.offset_x)

        # Display action touche
        # If distance between center of house & shop < half of his size :
        #     display_action_touch
        if (
            (abs((self.h.x + self.h.size[0]/2 + self.offset_x) - x) < self.h.size[0]/2)
            or
            (abs((self.s.x + self.s.size[0]/2 + self.offset_x) - x) < self.s.size[0]/2)
            ) :

            img = pygame.transform.scale(self.eimg, (72, 72))
            rect = img.get_rect()
            rect.center = (x + 60, ground_altitude - 250)
            pos = (x + 48, ground_altitude - 290)
            main_game.screen.blit(img, rect)
            font = pygame.font.Font(main_game.main_font_name, 48) # Charge la police
            text = font.render(pygame.key.name(main_game.key_action), True, 'black')
            main_game.screen.blit(text, pos)

        if main_game.touch_pressed.get(main_game.key_action, False) :
            
            # Search
            if abs((self.h.x + self.h.size[0]/2 + self.offset_x) - x) < self.h.size[0]/2:
                img = pygame.transform.scale(self.eimg, (72, 72))
                rect = img.get_rect()
                rect.center = (main_game.player.get_relativ_x(self.offset_x) + 60, ground_altitude - 250)
                main_game.screen.blit(img, rect)
                main_game.change_view(main_game.search_view)

            # Shop
            elif abs((self.s.x + self.s.size[0]/2 + self.offset_x) - x) < self.s.size[0]/2:
                img = pygame.transform.scale(self.eimg, (72, 72))
                rect = img.get_rect()
                rect.center = (main_game.player.get_relativ_x(self.offset_x) + 60, ground_altitude - 250)
                main_game.screen.blit(img, rect)
                main_game.change_view(main_game.shop_view)

            # Plant
            elif not main_game.player.plant :
                if main_game.player.sprout >= 1 :
                    if main_game.connect :
                        pass
                    else :
                        x = main_game.player.get_relativ_x(self.offset_x)
                        # Générer une liste de tous les arbres qui sont proche de l'endroit où le joueur veut planter une pousse
                        t = list(filter(lambda tree : abs(tree.x - x) < 100, self.trees))
                        if len(t) == 0 : # Vérifier si elle est vide
                            main_game.tuto.next("plant")
                            main_game.player.plant_act()
                            main_game.player.sprout -= 1
                            self.wait_tree = {'x' : main_game.player.x + (0 if main_game.player.orientation == "LEFT" else main_game.player.size[0]), 'y' : 0, 'type' : 'oak', 'fertilized': main_game.player.fertilizer > 0}
                            if main_game.player.fertilizer > 0 :
                                main_game.player.fertilizer -= 1
                        else :
                            main_game.player.say('Trop proche :/', 2_000)
                else :
                    main_game.player.say("Pas de pousse :/", 2_000)

        if main_game.player.move and pygame.time.get_ticks() - self.last_actualisation > 500 :
            self.last_actualisation = pygame.time.get_ticks()
            main_game.outbox.put({
                "type" : "pos",
                "pos" : main_game.player.x
            })

        if main_game.connect :
            while not main_game.inbox.empty():
                data = main_game.inbox.get()
                match data['type']:
                    case 'new_players' :
                        self.add_player(data['player'])
                    case 'start_move' :
                        self.players[data['username']].move = True
                        self.players[data['username']].orientation = data['direction']
                    case 'stop_move' :
                        self.players[data['username']].move = False
                        self.players[data['username']].x = data['pos']
                    case 'pos' :
                        self.players[data['username']].x = data['pos']
                    case 'new_tree':
                        for tree in self.trees:
                            if tree["x"] == data["x"]:
                                tree["skin_index"] = data["skin_index"]
                                tree["seedling"] = data["seedling"]
                                tree["growned_up"] = data["growned_up"]

        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.actual_decoration :
                    if self.actual_decoration.placing(self.offset_x, ground_rect[3]):
                        self.decorations.append(self.actual_decoration)
                    self.actual_decoration = None
                else :
                    self.actual_decoration = Decoration()
            
            if event.type == pygame.MOUSEWHEEL and self.actual_decoration :
                self.actual_decoration.change_type((main_game.scroll_y//10)%len(decoration_type))

            if event.type == pygame.KEYDOWN:
                if event.key == main_game.key_move_left:
                    main_game.player.orientation = "LEFT"
                    main_game.player.move = True
                    if main_game.connect :
                        main_game.outbox.put({
                            "type" : "start_move",
                            "direction" : "LEFT"
                        })
                if event.key == main_game.key_move_right:
                    main_game.player.orientation = "RIGHT"
                    main_game.player.move = True
                    if main_game.connect :
                        main_game.outbox.put({
                            "type" : "start_move",
                            "direction" : "RIGHT"
                        })
                if event.key == main_game.key_help:
                    main_game.tuto.help()
            if event.type == pygame.KEYUP:
                if event.key == main_game.key_move_left or event.key == main_game.key_move_right:
                    main_game.player.move = False
                    main_game.player.change_skin()
                    if main_game.connect :
                        main_game.outbox.put({
                            "type" : "stop_move",
                            "pos" : main_game.player.x
                        })
