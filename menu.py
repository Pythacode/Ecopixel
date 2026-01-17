# -------------------------------- Menu -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Lucas - https://github.com/GreGrenier                         #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

from game import *
import pygame

def init() :
    global font
    global text 

    pygame.init()
    text = "_"
    font = pygame.font.Font("freesansbold.ttf", 24)

def update(events, screen) :
    global text

    width, height = screen.get_size() 

    # Header
    pygame.draw.rect(screen, (255, 201, 157), (0, 0, width, 720), width=0)

    text_pygame = font.render("test", True, BLACK)
    screen.blit(text_pygame, (27, 27))

menuView = view(init, update)