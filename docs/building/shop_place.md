# shop_place.py
Permet d'afficher le shop

## Sommaire

- [Class Shop_place](#class-shop_place)
    - [Paramètres](#paramètres)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class Shop_place

### Paramètres

- `x` : Position x du shop dans le monde (250 de base)
- `y` : Position y du shop dans le monde (-10 de base)

### Attributs

- `image` : Image du tileset du shop
- `tilesetjson` : Fichier json qui donne les positions des sprites sur la tileset
- `size` : Tuple de 2 valeurs représentant la taille du shop sur l'axe x et y
- `right0 à 3` : Différents sprites pour l'animation de droite du shop
- `left0 à 3` : Différents sprites pour l'animation de gauche du shop
- `right_list` : Liste comportant tous les sprites de l'animation de droite du shop
- `left_list` : Liste comportant tous les sprites de l'animation de gauche du shop
- `actual_skin` : Le sprite actuellement affiché (initialement right0)
- `frame` : Frame de l'animation (ex : 0 = right0, 1 = right1, etc...)
- `last_change` : Tick à laquel le dernier changement de frame a eu lieu

### Fonctions

- `change_skin(offset_x)`: Permet de changer de sprite selon la position du joueur et la frame d'animation
- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher le shop et changer les frames d'animation dans le jeu<br>
    - `surface` : où on veut que le shop soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est le shop par rapport à la caméra