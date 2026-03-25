# Les vues du jeu

Une vue est une partie du jeu, comparable aux pages d'un site web : Chaque vue à un rôle précis dans le jeu.

Par exemple, le menu est géré par une vue, le menu de réglages aussi, etc...

Une vue est une `class` doit impérativement avoir les fonctions suivantes :

- `__init__(self)` :
    Cette fonction vas être appelé au démarrage du jeux[^1]. Elle doit initialiser les variables de la vue, déclarer les boutons, les inputs...

- `update(self, events)` :
    C'est la fonction que sera appelé à chaque tour de jeu quand la vue est affichée. Elle doit prendre un argument : la liste des évènements pygame. Elle doit gérer l'affichage, le mouvement des sprites... 

De plus, les variables suivante peuvent être ajoutés :

- `header` : Boléen qui indique si il faut afficher le header[^2]
- `self.max_scroll_y` : La limite maximum de scroll sur l'axe Y (Si la valeur est égale à 0, le scroll ne pourra pas monter)
- `self.min_scroll_y` : La limite minimum de scroll sur l'axe Y (Si la valeur est égale à 0, le scroll ne pourra pas decendre)
- `self.max_scroll_x` : La limite maximum de scroll sur l'axe X (Si la valeur est égal à 0, le scroll ne pourra pas aller à gauche)
- `self.min_scroll_x` : La limite minimum de scroll sur l'axe X (Si la valeur est égale à 0, le scroll ne pourra pas droite)

[^1]: Note : Dans les futures versions du jeu, cette fonction sera appelée au premier affichage de la vue.
[^2]: Voir la [fonction `draw_header`](game.md#fonction-draw_header)

## Les vues existantes

- `GameView` : Vue du jeu en lui-même
- `menu` : Vue du menu
- `searchEngine` : Vue du moteur de recherche
- `settings` : Vue du menu paramètre
- `shop` : Vue du shop