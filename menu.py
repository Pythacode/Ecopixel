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

def PlayButton_Pressed():
    print("CLIQUEEEEEEEEEE")

def QuitButton_Pressed():
    #makes an error on "pygame.display.flip()"... To fix it we should change the running var but I can't acces it !
    pygame.quit()

def init() :
    global font
    global text

    pygame.init()
    text = "_"
    font = pygame.font.Font("freesansbold.ttf", 24)

def update(events) :
    global text

    width, height = main_game.screen.get_size() 

    # Header
    pygame.draw.rect(main_game.screen, (255, 201, 157), (0, 0, width, 720), width=0)

    # Logo
    image = pygame.image.load(os.sep.join(["assets", "logo.png"]))
    scaled_image = pygame.transform.scale(image, (48*4, 48*4))
    rect = scaled_image.get_rect()
    rect.center = (640, 200)
    main_game.screen.blit(scaled_image, rect)

    # Play button
    playbutton = button(os.sep.join(["assets", "play_button_nor.png"]), os.sep.join(["assets", "play_button_mouse.png"]), os.sep.join(["assets", "play_button_click.png"]), (640, 360), 48*4, 24*4, PlayButton_Pressed, text="")
    playbutton.createButton(main_game.screen)

    # Quit button
    quitbutton = button(os.sep.join(["assets", "button_nor.png"]), os.sep.join(["assets", "button_mouse.png"]), os.sep.join(["assets", "button_click.png"]), (640, 460), 48*4, 24*4, QuitButton_Pressed, text="Quit")
    quitbutton.createButton(main_game.screen)

menuView = view(init, update)