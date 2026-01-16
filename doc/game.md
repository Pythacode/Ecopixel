# Game.py
Définit les variable globals

## view

Crée une classe qui prend en argument d’initialisation deux fonctions :
- Une fonction `init` : Une fonction qui sert à initialiser la vue.. Elle doit attendre aucun argument et seras apeller à chaque fois que la vue vas être afficher. Les variable déclarer dedant doivent être déclarré en début de fontion avec `global`.
- Une fonction `update` : Une fonction qui sert à gérer actualiser la vue.. Elle doit attendre deux argument, la liste d'évènement et un objet surface qui correspond à l'écran.