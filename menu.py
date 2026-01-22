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
    pass

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

    # Play button
    playbutton = button(os.sep.join(["assets", "play_button_nor.png"]), os.sep.join(["assets", "play_button_mouse.png"]), os.sep.join(["assets", "play_button_click.png"]), (width/2, height/2), 48*4, 24*4, PlayButton_Pressed, text="")
    playbutton.createButton(main_game.screen)

menuView = view(init, update)