# -------------------------------- Menu -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Lucas - https://github.com/GreGrenier                         #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

from game import *
import pygame
import os
from view import view
from gameView import gameView


class menuView():

    def PlayButton_Pressed(self):
        main_game.change_view(gameView)

    def QuitButton_Pressed(self):
        main_game.running = False 

    def Logo_Pressed(self):
        babysfx = pygame.mixer.Sound(os.sep.join(["assets", "sfx", "BabyNoise.mp3"]))
        babysfx.play()

    def init(self) :

        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 24)

        # Logo init
        self.logo = button(os.sep.join(["assets", "image", "logo.png"]), os.sep.join(["assets", "image", "logo.png"]), os.sep.join(["assets", "image", "logo.png"]), (640, 200), 48*4, 48*4, self.Logo_Pressed)
        self.logo.createButton()

        # Play button init
        self.playbutton = button(os.sep.join(["assets", "image", "button", "play_button_nor.png"]), os.sep.join(["assets", "image", "button", "play_button_mouse.png"]), os.sep.join(["assets", "image", "button", "play_button_click.png"]), (640, 360), 48*4, 24*4, self.PlayButton_Pressed, text="")
        self.playbutton.createButton()

        # Quit button init
        self.quitbutton = button(os.sep.join(["assets", "image", "button", "button_nor.png"]), os.sep.join(["assets", "image", "button", "button_mouse.png"]), os.sep.join(["assets", "image", "button", "button_click.png"]), (640, 460), 48*4, 24*4, self.QuitButton_Pressed, text="Quit")
        self.quitbutton.createButton()


    def update(self, events) :

        width, height = main_game.screen.get_size() 

        # Header
        pygame.draw.rect(main_game.screen, (255, 201, 157), (0, 0, width, 720), width=0)

        
        self.logo.update(main_game.screen)
        self.playbutton.update(main_game.screen)
        self.quitbutton.update(main_game.screen)

        
