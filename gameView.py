# --------------------------- Search engine ---------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
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
    def __init__(self):
        self.offset_x = 0
        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "game", "ground.png"]))
        self.draw_element = []
        self.last_frame = 0
        self.header = True

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
        if main_game.touch_pressed.get(main_game.key_plant, False) and not main_game.player.plant:
            main_game.player.plant_act()
            self.draw_element.append(Tree(main_game.player.x, height - ground_rect[3]))

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
        
        for elem in filter(lambda e : -e.rect[2] <= e.x + self.offset_x <= width, self.draw_element) :
            elem.rect = pygame.Rect(elem.x+self.offset_x, height-elem.rect[3]-ground_rect[3], *elem.rect[2:4])
            main_game.screen.blit(elem.image, elem.rect)
            elem.draw(main_game.screen, height - ground_rect[3])

        main_game.player.draw(main_game.screen, height - ground_rect[3])

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
