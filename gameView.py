from game import *
import os

class Player() :
    def __init__(self, center):
        self.passiv_skin = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player", "static_player.png"]))
        self.actual_skin = self.passiv_skin
        self.size = self.actual_skin.get_rect()[2:4]
        
        self.x = center - (self.actual_skin.get_rect()[2] / 2)
        self.y = 0

        self.velocity = 5

    def draw(self, surface, ground_altitude) :
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x, ground_altitude + self.y - rect[3]
        surface.blit(self.actual_skin, rect)

    def move_left(self) :
        self.x -= self.velocity

    def move_right(self) :
        self.x += self.velocity

class gameView() :
    def __init__(self):
        self.player = Player(main_game.screen.get_size()[0] / 2)
        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "ground.png"]))

    def update(self, events) :
        main_game.screen.fill(main_game.WHITE)

        rect = self.ground.get_rect()
        width, height = main_game.screen.get_size()

        # Draw ground
        x = 0
        while x < width :
            rect[0], rect[1] = x, height - rect[3]
            main_game.screen.blit(self.ground, rect)
            x += rect[2]

        # Move player
        if main_game.touch_pressed.get(pygame.K_LEFT, False) :
            if self.player.x > 200 :
                self.player.move_left()
        if main_game.touch_pressed.get(pygame.K_RIGHT, False) :
            if self.player.x < width - self.player.size[1] :
                self.player.move_right()

        self.player.draw(main_game.screen, height - rect[3])