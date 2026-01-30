from game import *
import os

class Player() :
    def __init__(self, center):
        self.passiv_skin = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player", "static_player.png"]))
        self.tileset = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "player_tileset.png"]))

        self.file_size = (44, 46)
        self.size = (200, 200)

        self.static_one = self.tileset.subsurface(0,0, *self.file_size)
        self.static_one = pygame.transform.scale(self.static_one, self.size)
        self.static_two = self.tileset.subsurface(44,0, *self.file_size)
        self.static_two = pygame.transform.scale(self.static_two, self.size)

        self.move_one = self.tileset.subsurface(2*self.file_size[0],0, *self.file_size)
        self.move_one = pygame.transform.scale(self.move_one, self.size)
        self.move_two = self.tileset.subsurface(3*self.file_size[0],0, *self.file_size)
        self.move_two = pygame.transform.scale(self.move_two, self.size)

        self.static_skin_list = (self.static_one, self.static_two)
        self.move_skin_list = (self.move_one, self.move_two)

        self.actual_skin = self.static_one
        self.skin_index = 0
        
        self.x = center - (self.file_size[0] / 2)
        self.y = 0
        self.orientation = "RIGHT"

        self.velocity = 5
        self.last_change = pygame.time.get_ticks()
        self.move = False

    def change_skin(self) :
        now = pygame.time.get_ticks()
        if now - self.last_change > (15*self.velocity if self.move else 500) :
            self.last_change = now
            self.skin_index = not self.skin_index
            if self.move :
                skin_list = self.move_skin_list
            else :
                skin_list = self.static_skin_list
            self.actual_skin = skin_list[self.skin_index]

    def draw(self, surface, ground_altitude) :
        self.change_skin()
        rect = self.actual_skin.get_rect()
        rect[0], rect[1] = self.x, ground_altitude + self.y - rect[3]
        surface.blit(pygame.transform.flip(self.actual_skin, True, False) if self.orientation == "LEFT" else self.actual_skin, rect)

    def move_left(self) :
        self.move = True
        self.x -= self.velocity

    def move_right(self) :
        self.move = True
        self.x += self.velocity

class gameView() :
    def __init__(self):
        self.offset_x = 0
        self.player = Player(main_game.screen.get_size()[0] / 2)
        self.ground = pygame.image.load(os.sep.join([main_game.asset_doc, "image", "ground.png"]))

    def update(self, events) :
        main_game.screen.fill(main_game.WHITE)

        rect = self.ground.get_rect()
        width, height = main_game.screen.get_size()

        # Draw ground
        x = - rect[2]
        ground_offset = self.offset_x % rect[2] # ground offset
        while x < width :
            rect[0], rect[1] = x + ground_offset, height - rect[3]
            main_game.screen.blit(self.ground, rect)
            x += rect[2]

        # Move player
        if main_game.touch_pressed.get(pygame.K_LEFT, False) :
            if self.player.x > 200 :
                self.player.move_left()
            else :
                self.offset_x += self.player.velocity
        if main_game.touch_pressed.get(pygame.K_RIGHT, False) :
            if self.player.x < width - self.player.size[1] - 200 :
                self.player.move_right()
            else :
                self.offset_x -= self.player.velocity

        self.player.draw(main_game.screen, height - rect[3])

        for event in events :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    self.player.orientation = "LEFT"
                    self.player.move = True
                if event.key == pygame.K_RIGHT :
                    self.player.orientation = "RIGHT"
                    self.player.move = True
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    self.player.move = False
                    self.player.change_skin()