# game.py
Définit les variable & les fonction globale

## Somaire

- [Class Game](#class-game)
    - [Paramètre](#paramètre)
    - [Attributs](#attribut)
    - [Fonctions](#fonctions)

## Class Game

Il s'agit d'une class qui contient les variables globals du jeux.

### Paramètre

- `WIDTH` : Un entier qui défini la largeur de la fenètre (en pixel)
- `HEIGHT` : Un entier qui défini la hauteur de la fenètre (en pixel)

### Attribut

- `asset_doc` : Le dossier des assets
- `data` : Les données de la sauvegarde JSON, un dictionaire vide si elle n'exsiste pas
- `scren` : Écran principal du jeux
- `current_view` : Vue actuellement affiché à l'écran
- `WHITE` et `BLACK` : Couleurs RGB
- `running` : Indique si le jeux tourne
- `main_font_name` : Nom de la police de base du jeux 
- `scroll_x` et `scroll_y` : Décalage en x et y du à la molette de la souris
- `touch_pressed` : Un dictionaire avec toute les touche actuellement pressé. Pour savoir si la touche est pressé : `self.touch_pressed.get(<TOUCHE PYGAME>, False)`
- `logo` : Image du logo du jeu
- `back` : Image de la flèche retour du jeu
- `player` : Le joueur
- `key_move_right`, `key_move_left`, `key_plant` : Touche enregistré ou par défault.

### Fonctions

- change_view<br>
    Modifie la vue actuelle

## Class entry_text

Il s'agit d'une class qui ajoute une zone de texte

### Paramètre

- `surface` : Écran où est affiché la zone de texte
- `color` : Couleur de la bordure
- `pos` : Position de la zone de texte
- `size`: Taille de la zone de texte
- `width` : Épaisseur de la bordure
- `border_radius`: Dureté des coin de la bordure
- `font`: Police du texte

### Attribut

- `active` : Si la zone de texte est active
- `text` : Liste qui contient le texte avec un caractère par élément
- `font` : Police du texte
- `x` et `y` : Position du texte
- `color` : Couleur de la bordure
- `surface` : Écran où est affiché la zone de texte
- `width` : Épaisseur de la bordure
- `border_radius` : Dureté des coin de la bordure
- `search_zone` : Zone de texte sous forme de `Rect` pygame
- `last_change` : Durée en miliseconde depuis le dernier changement du curseur
- `cursor` : Faut-il afficher le curseur
- `cursor_index` : index du curseur

### Fonctions

- update<br>
    Fonction à appeller à chaque boucle du jeu, elle actualise la zone de texte.

## Fonction draw_header

Fonction qui crée et affiche le header. doit être apellée à chaque tour du jeu.

## Variable main_game

Un élément [Game](#class-game) avec plusieur vues qui sont définie.