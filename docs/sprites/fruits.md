# fruits.py
Permet d'afficher la maison

## Sommaire

- [Class Fruit](#class-fruit)
    - [Paramètres](#paramètres)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class Fruit

### Paramètres

- `x` : Position x de la maison dans le monde (0 par défaut)
- `y` : Position y de la maison dans le monde (0 par défaut)
-  `type` : Type de fruit ("apple" par défaut)

### Attributs

- `size` : Tuple de 2 valeurs représentant la taille du fruit sur l'axe x et y
- `apple` : Image de la pomme (data\image\icon\fruits.png)
- `actual_skin` : Le sprite actuellement affiché ("apple" par défaut)

### Fonctions

- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher le fruit dans le jeu et gérer sa récupération.<br>
    - `surface` : où on veut que le fruit soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est le fruit par rapport à la caméra