# Main.py

Ce fichier est le noyau du jeu, il contient le code pygame commun à toutes les vues

Il crée une fenêtre de jeu puis crée une boucle de jeux qui :


- Écoute les évènements :
    - Si c’est un événement QUIT il ferme le jeu.
    - Si c'est keydown ou keyup, il actualiser un dictionaire ou toute les touche actuellement pressé on comme valeur `True`. Il vérifie également si lla touche pressé est celle pour sauvegarder.
    - Si c'est un évènement de la molette, on actualise une variable qui contient la valeur actuelle du scroll, en restant dans la limite imposé si elle exsiste.
    Les évènement sont aussi transmis à la vue actuelle via `update()`

- Caclule Δt entre 2 frames
- Actualise la vue actuelle via `update()`
- Actualise la fenêtre

Et, quand le jeux se femre, sauvegarde et ferme proprement le jeux.
Si l'utilisateur ferme le jeux avec `Ctrl+C` via le terminal, la sauvegarde est quand même faite.