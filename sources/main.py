# ------------------------- Fichier Principal -------------------------- #
# Lien du dépot : http://github.com/Pythacode/Ecopixel                   #
# Fichier contenant tout le code de la boucle principal du jeu.          #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License : GPL v3+ - https://www.gnu.org/licenses/gpl-3.0.fr.html       #
# ---------------------------------------------------------------------- #

import pygame
from game import *

last_frame = 0

# Boucle principal du jeu
while main_game.running:
    try :

        events = pygame.event.get()

        # Écout des évenement
        for event in events:
            # Quand l'utilisateur ferme la fenetre
            if event.type == pygame.QUIT:
                main_game.running = False
            
            # Lorsque l'utilisateur scroll
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
                if event.key == main_game.key_save :
                    if main_game.connect :
                        main_game.outbox.put({
                            "type" : "save"
                        })
                    else :
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
        if main_game.current_view.header : # Si la vue nécessite l'affichage du header
            draw_header()

        # Actualiser l'écran
        pygame.display.flip()
    except KeyboardInterrupt :
        print(f"Fermeture via une commande clavier")
        break

# Sauvegarde des données
main_game.save()

pygame.quit()
