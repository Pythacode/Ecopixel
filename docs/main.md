# Main.py

Ce fichier est le noyau du jeu, il contient le code pygame commun à toutes les vues

Il crée une fenêtre de jeu puis crée une boucle de jeu qui :


- Écoute les évènements :
    - Si c’est un événement QUIT il ferme le jeu.
    - Si c'est keydown ou keyup, il actualise un dictionaire où toutes les touches actuellement pressées ont comme valeur `True`. Il vérifie également si la touche pressée est celle pour sauvegarder.
    - Si c'est un évènement de la molette, on actualise une variable qui contient la valeur actuelle du scroll, en restant dans la limite imposé si elle existe.
    Les évènement sont aussi transmis à la vue actuelle via `update()`

- Calcul Δt entre 2 frames
- Actualise la vue actuelle via `update()`
- Actualise la fenêtre

Et, quand le jeu se ferme, sauvegarde et ferme proprement le jeu.
Si l'utilisateur ferme le jeu avec `Ctrl+C` via le terminal, la sauvegarde est quand même faite.