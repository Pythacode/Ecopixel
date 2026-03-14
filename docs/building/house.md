# house.py
Permet d'afficher la maison

## Sommaire

- [Class House](#class-house)
    - [Paramètres](#paramètres)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class House

### Paramètres

- `x` : Position x de la maison dans le monde (0 de base)
- `y` : Position y de la maison dans le monde (0 de base)
-  `lvl` : Niveau de la maison (prendra la valeur dans le fichier de sauvegarde)

### Attributs

- `size` : Tuple de 2 valeurs représentant la taille de la maison sur l'axe x et y
- `house1` : 1er sprite de la maison (data\image\houses\house1.png)
- `house2` : 2e sprite de la maison (data\image\houses\house2.png)
- `house3` : 3e sprite de la maison (data\image\houses\house3.png)
- `house4` : 4e sprite de la maison (data\image\houses\house4.png)
- `actual_skin` : Le sprite actuellement affiché (initialement house1)
- `all_houses` : Liste ayant tous les sprites de maison

### Fonctions

- `change_skin()` : change `actual_skin` en prenant la valeur d'index `lvl - 1` dans la liste `all_houses`
- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher la maison dans le jeu<br>
    - `surface` : où on veut que la maison soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est la maison par rapport à la caméra