# -------------------------------- Menu -------------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Lucas - https://github.com/GreGrenier                         #
# License : Creative Commons Attribution-NonCommercial 4.0 International #
# ---------------------------------------------------------------------- #

from game import *
import pygame
import os

def init() :
    global font
    global text
    global button_cooldown
    button_cooldown = 0 

    pygame.init()
    text = "_"
    font = pygame.font.Font("freesansbold.ttf", 24)

def update(events, screen) :
    global text
    global button_cooldown

    width, height = screen.get_size() 

    # Header
    pygame.draw.rect(screen, (255, 201, 157), (0, 0, width, 720), width=0)

    while button_cooldown > 0:
        button_cooldown -= 1
        pygame.time.wait(1)

    # Play button
    if createButton(os.sep.join(["assets", "play_button_nor.png"]), os.sep.join(["assets", "play_button_mouse.png"]), os.sep.join(["assets", "play_button_click.png"]), screen, (width/2, height/2), 48*4, 24*4, events) == True:
        pass

def createButton(image_nor, image_mouse, image_click, screen, position, width, height, events):
    global button_cooldown
    click = False
    image = pygame.image.load(image_nor)
    scaled_image = pygame.transform.scale(image, (width, height))
    rect = scaled_image.get_rect()
    rect.center = position
    if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        image = pygame.image.load(image_mouse)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                button_cooldown = 80
                click = True
                image = pygame.image.load(image_click)
    scaled_image = pygame.transform.scale(image, (width, height))
    screen.blit(scaled_image, rect)
    return click
    

menuView = view(init, update)