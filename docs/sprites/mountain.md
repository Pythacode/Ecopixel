# mountain.py
Permet d'afficher la maison

## Sommaire

- [Class Mountain](#class-mountain)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class Mountain

### Attributs

- `size` : Tuple de 2 valeurs représentant la taille du nuage sur l'axe x et y$
- `mountain`: Sprite des montagnes
- `x`: Position x du nuage dans le monde. (un chiffre aléatoire entre -100000 et 100000 par défaut)
- `y`: Position y du nuage dans le monde. (0 par défaut)
- `actual_skin` : Le sprite actuellement affiché. ("mountain" par défaut)

### Fonctions

- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher les nuages dans le jeu.<br>
    - `surface` : où on veut que le fruit soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est le fruit par rapport à la caméra. (qui ici est divisé par 3 pour donner l'effet de profondeur)