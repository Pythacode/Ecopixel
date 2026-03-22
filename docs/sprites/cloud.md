# cloud.py
Permet d'afficher la maison

## Sommaire

- [Class Cloud](#class-cloud)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class Cloud

### Attributs

- `size` : Tuple de 2 valeurs représentant la taille du nuage sur l'axe x et y$
- `cloud1-3`: Image des différents nuages.
- `x`: Position x du nuage dans le monde. (un chiffre aléatoire entre -100000 et 100000 par défaut)
- `y`: Position y du nuage dans le monde. (un chiffre aléatoire entre 450 et 500 par défaut)
- `cloud_skin`: Liste avec pour valeurs "cloud1-3".
- `actual_skin` : Le sprite actuellement affiché. (un sprite aléatoire qui est dans la liste "cloud_skin" par défaut)

### Fonctions

- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher les nuages dans le jeu.<br>
    - `surface` : où on veut que le fruit soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est le fruit par rapport à la caméra. (qui ici est divisé par 2 pour donner l'effet de profondeur)