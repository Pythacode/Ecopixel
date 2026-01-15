# Main.py

Ce fichier est le noyau du jeu, il contient le code pygame commun à toutes les vues

Il crée une fenêtre de jeu puis crée une boucle de jeux qui :
- Écoute les évènements. Si c’est un événement QUIT il ferme le jeu, sinon il transmet à la vue actuelle via la fonction update
- Actualise la vue actuelle
- Actualise la fenêtre