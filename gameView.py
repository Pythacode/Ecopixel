from game import *
import os

class Player() :
    def __init__(self, center):
        self.passiv_skin = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player", "static_player.png"]))
        self.actual_skin = self.passiv_skin
        
        self.x = center - (self.actual_skin.get_rect()[2] / 2)
        self.y = 0

    def draw(self, surface, ground_altitude) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x, ground_altitude + self.y - rect[3]
        surface.blit(self.actual_skin, rect)

class gameView() :
    def __init__(self):
        self.player = Player(main_game.screen.get_size()[0] / 2)
        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "ground.png"]))

    def update(self, events) :
        main_game.screen.fill(main_game.WHITE)

        rect = self.ground.get_rect()
        
        width, height = main_game.screen.get_size()

        x = 0
        while x < width :
            rect[0], rect[1] = x, height - rect[3]
            main_game.screen.blit(self.ground, rect)
            x += rect[2]

        self.player.draw(main_game.screen, height - rect[3])