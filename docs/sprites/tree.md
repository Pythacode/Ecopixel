# tree.py
Fichier contenant tout le code des arbres

## Sommaire

- [Class Tree](#class-tree)
    - [Paramètres](#paramètres)
    - [Attributs](#attributs)
    - [Fonctions](#fonctions)

## Class Tree

### Paramètres

- `x` : Position x de l'arbre dans le monde (prend la position de l'arbre dans le fichier de sauvegarde ou la position où le joueur plante)
- `y` : Position y de l'arbre dans le monde (0 par défaut)
-  `type` : Type de l'arbre en str (oak par défaut)
- `fertilized` : True si lors du plantage le joueur possédait au moins un engrais. (False par défaut)
- `time_alive` : Durée depuis le plantage de l'arbre ou depuis le dernier changement d'état.
- `seedling` : True si l'arbre est encore une pousse.
- `growned_up` : True si l'arbre a fini sa croissance.
- `skin_index` : Index du sprite associé à l'arbre.
- `max_alive` : Temps qu'il faut pour passer d'un stage à l'autre. (Un nombre entre 900 et 1200 par défaut et entre 600 et 900 si "fertilized" est égal True)

### Attributs

- `size` : Tuple de 2 valeurs représentant la taille d'un arbre sur l'axe x et y
- `seedling0-4` : Différents sprites des pousses.
- `oak0-4`: Différents sprites des arbres.
- `seedling_skin_list`: Liste de tous les sprites des pousses.
- `oak_skin_list`: Liste de tous les sprites des chênes.
- `apple_spawn`: Int qui s'incrément de 1 toutes les frames si "growned_up" est égal à True. Quand "apple_spawn" est égal à "max_apple", la variable est mise à 0 et une pomme apparaît
- `max_apple`: Chiffre aléatoire entre 900 et 1200.
- `skin_list` : Liste de sprites actuellement utilisé. (ex: seedling_skin_list si "seedling" est True)
- `actual_skin`: Le sprite actuellement utilisé. (prend le sprite de "skin_list" par l'index "skin_index" par défaut)

### Fonctions

- `change_skin()` : ajoute 1 à "skin_index" puis vérifie les états de l'arbre et enfin change "actual_skin".
- `draw(surface ,ground_altitude, offset_x)` : Fonction permettant d'afficher l'arbre dans le jeu et gère son vieillissement.<br>
    - `surface` : où on veut que l'arbre soit afficher (`main_game.screen` est recommandé)
    - `ground_altitude` : hauteur du sol
    - `offset_x` : où est l'arbre par rapport à la caméra