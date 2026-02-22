# button class
Permet de créer des boutons

## Sommaire

- [init] (#func-init)
- [update] (#func-update)

## init
- `image_nor` : Image du bouton quand aucune action n'est effectué. Format : os.sep.join([])
- `image_mouse` : Image du bouton quand la souris est dessus. Format : os.sep.join([])
- `image_click` : Image du bouton quand il est cliqué. Format : os.sep.join([])
- `position` : Position du bouton. Format : tuple
- `width` : Largeur du bouton (devrait être un multiple de la largeur de l'image). Format : int
- `height` : Hauteur du bouton (devrait être un multiple de la hauteur de l'image). Format : int
- `OnClickFunc` : Fonction appelé quand le bouton est appuyé.
- `text`: Texte affiché sur le bouton (debug). Format : str; Par défaut : ""

## update
- `screen` : main_game.screen
- `position` : Position du bouton (pour le responsive). Format : tuple