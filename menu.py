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

def init() :
    global font
    global text
    global button_cooldown
    button_cooldown = 0 

    pygame.init()
    text = "_"
    font = pygame.font.Font("freesansbold.ttf", 24)

def update(events) :
    global text
    global button_cooldown

    width, height = main_game.screen.get_size() 

    # Header
    pygame.draw.rect(main_game.screen, (255, 201, 157), (0, 0, width, 720), width=0)

    while button_cooldown > 0:
        button_cooldown -= 1
        pygame.time.wait(1)

    # Play button
    button.__init__(play, os.sep.join(["assets", "play_button_nor.png"]), os.sep.join(["assets", "play_button_mouse.png"]), os.sep.join(["assets", "play_button_click.png"]), (width/2, height/2), 48*4, 24*4)
    #(os.sep.join(["assets", "play_button_nor.png"]), os.sep.join(["assets", "play_button_mouse.png"]), os.sep.join(["assets", "play_button_click.png"]), (width/2, height/2), 48*4, 24*4, events)
    

menuView = view(init, update)