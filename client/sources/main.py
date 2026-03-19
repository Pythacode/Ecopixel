# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code du moteur de jeu.                       #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import pygame
import json
from game import *
import socket
import sys

last_frame = 0

# Connection au serveur
if os.path.exists(os.sep.join([main_game.asset_doc, "server_config.json"])) :
    serverJsonfile = open(os.sep.join([main_game.asset_doc, "server_config.json"]), 'r') 
    serverConfig = json.load(serverJsonfile)
else :
    serverConfig = {}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverConfig.get("HOST", "127.0.0.1"), serverConfig.get("IP", 2123)))

message = {
    "type" : 'init',
    'version' : '1'
}
message = json.dumps(message)
client.send(message.encode('utf-8'))

messagerecv = client.recv(1124).decode('utf-8')
messagerecv = json.loads(messagerecv)

if not messagerecv['accept'] :
    print("Connexion impossible\nLa version de votre client n'est pas compatible avec le serveur.")
    pygame.quit()
    sys.exit()

# Boucle principal du jeu
while main_game.running:
    try :

        events = pygame.event.get()

        # Écout des évenement
        for event in events:
            # Quand l'utilisateur ferme la fenetre
            if event.type == pygame.QUIT:
                main_game.running = False
            
            # Losrque l'utilisateur scrolle
            elif event.type == pygame.MOUSEWHEEL:
                if hasattr(main_game.current_view, "min_scroll_y") and event.y > 0 :
                    if main_game.current_view.min_scroll_y < main_game.scroll_y - event.y * 10 :
                        main_game.scroll_y -= event.y * 10
                    else :
                        main_game.scroll_y = main_game.current_view.min_scroll_y
                elif hasattr(main_game.current_view, "max_scroll_y") and event.y < 0 :
                    if main_game.current_view.max_scroll_y > main_game.scroll_y - event.y * 10 :
                        main_game.scroll_y -= event.y * 10
                    else :
                        main_game.scroll_y = main_game.current_view.max_scroll_y
                else :
                    main_game.scroll_y -= event.y * 10
                    
                if hasattr(main_game.current_view, "min_scroll_x") and event.x > 0 :
                    if main_game.current_view.min_scroll_x < main_game.scroll_x - event.x * 10 :
                        main_game.scroll_x -= event.x * 10
                    else :
                        main_game.scroll_x = main_game.current_view.min_scroll_x
                elif hasattr(main_game.current_view, "max_scroll_x") and event.x < 0 :
                    if main_game.current_view.max_scroll_x > main_game.scroll_x - event.x * 10 :
                        main_game.scroll_x -= event.x * 10
                    else :
                        main_game.scroll_x = main_game.current_view.max_scroll_x
                else :
                    main_game.scroll_x -= event.x * 10

            # lorsqu'il appuie sur une touche
            elif event.type == pygame.KEYDOWN :
                main_game.touch_pressed[event.key] = True # Met `TRUE` à la clé `event.key`
                # Si la touche est la touche de sauvegarde
                if event.key == main_game.key_save : # On lance la sauvegarde
                    main_game.save()

            # Lorsqu'il relache la touche
            elif event.type == pygame.KEYUP :
                main_game.touch_pressed[event.key] = False # Met `TRUE` à la clé `event.key`

        # Calculate delta time
        now = pygame.time.get_ticks()
        main_game.dt =  (now - last_frame)
        last_frame = now

        # Gérer le rendu
        main_game.current_view.update(events)
        if main_game.current_view.header : # Si la vue nécésite l'affichage du header
            draw_header()

        # Actualiser l'écran
        pygame.display.flip()
    except KeyboardInterrupt :
        print(f"Fermeture via une commande clavier")
        break

# Sauvegarde des données
main_game.save()

pygame.quit()
