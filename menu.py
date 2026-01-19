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


    createButton("assets/play_button_nor.png", "assets/play_button_mouse.png", "assets/play_button_click.png",screen, (width/2, height/2), (48*4,24*4))

def createButton(image_nor, image_mouse, image_click, screen, position, size):
    if pygame.mouse.get_pos > position - size and pygame.mouse.get_pos < position - size:
        image = pygame.image.load(image_mouse)
    else:
        image = pygame.image.load(image_nor)
    scaled_image = pygame.transform.scale(image, size)
    rect = scaled_image.get_rect()
    rect.center = position
    screen.blit(scaled_image, rect)
    

menuView = view(init, update)