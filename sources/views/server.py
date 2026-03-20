# -------------------------------- Menu -------------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du menu de connection.                  #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

from game import *
import pygame
import os

class serverView():

    def __init__(self) :

        pygame.init()

        # Join button init
        self.serverbutton = button(os.sep.join([main_game.asset_doc, "image", "button", "button_nor.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_mouse.png"]), os.sep.join([main_game.asset_doc, "image", "button", "button_click.png"]), (640, 600), 48*4, 24*4, self.serverButton_Pressed, text="Jouer")
        
        width, height = main_game.screen.get_size() 
        self.width_cont = 500
        self.font = pygame.font.Font(main_game.main_font_name, 24)
        self.little_font = pygame.font.Font(main_game.main_font_name, 14)

        self.hostname_entry = entry_text(main_game.screen, 'black', (width/2-self.width_cont/2, 280), (3*(self.width_cont/4)-5, 40), 2, 25, self.font, backround_color='white')
        self.port_entry = entry_text(main_game.screen, 'black', (width/2+self.width_cont/4, 280), (self.width_cont/4-5, 40), 2, 25, self.font, backround_color='white')


        self.username_entry = entry_text(main_game.screen, 'black', (width/2-self.width_cont/2, 380), (self.width_cont, 40), 2, 25, self.font, backround_color='white')
        self.password_entry = entry_text(main_game.screen, 'black', (width/2-self.width_cont/2, 480), (self.width_cont, 40), 2, 25, self.font, backround_color='white', replace="·")

        serverJsonPath = os.path.sep.join([main_game.asset_doc, "server_config.json"])

        if os.path.exists(serverJsonPath) :
            serverJsonfile = open(serverJsonPath, 'r') 
            serverConfig = json.load(serverJsonfile)
        else :
            serverConfig = {}

        self.hostname_entry.text = list(serverConfig.get("HOST", "127.0.0.1"))
        self.port_entry.text = list(str(serverConfig.get("PORT", 2123)))

        self.header = False
        self.previous_view = None

    def serverButton_Pressed(self):
        main_game.change_view(main_game.server_view)

    def update(self, events) :

        width, height = main_game.screen.get_size() 

        # Header
        main_game.screen.fill((255, 201, 157))

        #logo = pygame.image.load(main_game.logo)
        scaled_image = pygame.transform.scale(main_game.logo, (192, 192))
        rect = scaled_image.get_rect()

        rect.center = (width/2, 150)
        main_game.screen.blit(scaled_image, rect)

        # Connection
        hostname_text = self.font.render("Hostname", True, 'black')
        main_game.screen.blit(hostname_text, (width/2-self.width_cont/2+5, 250))
        port_text = self.font.render("Port", True, 'black')
        main_game.screen.blit(port_text, (width/2+self.width_cont/4+10, 250))

        self.hostname_entry.update(events, (width/2-self.width_cont/2, 280), (3*(self.width_cont/4)-5, 40))
        self.port_entry.update(events, (width/2+self.width_cont/4, 280), (self.width_cont/4-5, 40))
        
        hostname_text = self.font.render("Nom d'utilisateur", True, 'black')
        main_game.screen.blit(hostname_text, (width/2-self.width_cont/2+5, 350))
        port_text = self.font.render("Mot de passe", True, 'black')
        main_game.screen.blit(port_text, (width/2-self.width_cont/2+5, 450))

        self.username_entry.update(events, (width/2-self.width_cont/2, 380), (self.width_cont, 40))
        self.password_entry.update(events, (width/2-self.width_cont/2, 480), (self.width_cont, 40))

        port_text = self.little_font.render("Si aucun compte n'est associé à ce nom d'utilisateur, il seras créer.", True, 'black')
        main_game.screen.blit(port_text, (width/2-self.width_cont/2+5, 530))

        self.serverbutton.update(main_game.screen, ((width/2), 600))
        
