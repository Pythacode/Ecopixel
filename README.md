# ecosia_simulator

Un jeu où l'on peut planter des arbres en achetant des pousses grace au crédits que l'on gagnerais en fesant des recherches sur le web

## Sommaire

- [Instalation](#instalation)
- [Lancement](#lancement)
    - [Avec venv](#avec-venv)
    - [Sans venv](#sans-venv)

## Instalation

> [!TIP]
> Dans ce README, nous utiliserons les commandes `python3` et `pip`. Cepeandant, suivant votre instalation, vous devrier peut être utiliser `python` et `python3 -m pip` à la place.

## Lancement

### Avec venv

[Documentation officiel](https://docs.python.org/3/library/venv.html "Documentation officiel venv")

Pour commencer, if faut créer un venv avec la commande suivante en étant dans le répertoire racine du projet:
```shell
python3 -m venv venv
```

Ensuite, il faut renter dans l'environnement virtuel. Pour cela, utilisez la commande qui correspond à votre shell :
  
* POSIX (Linux, MacOS...)

    | Shell | Commande pour activer l'environement virtuel | 
    | - | - |
    | bash/zsh | `$ source venv/bin/activate` |
    | fish | `$ source venv/bin/activate.fish` |
    | csh/tcsh | `$ source venv/bin/activate.csh` |
    | pwsh | `$ venv/bin/Activate.ps1` |

* Windows

    | Shell | Commande pour activer l'environement virtuel |
    | - | - |
    | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
    | PowerShell | `PS C:\> venv\Scripts\Activate.ps1` |

Ensuite, installez les dépendence avec 

```
pip install -r requirements.txt
```

Enfin, lancez simplement le projet avec la commande

```shell
python3 main.py
```
    
### Sans venv

Pour commencer, installez les modules avec la commande :

```
pip install -r requirements.txt
```

Enfin, lancez simplement le projet avec la commande

```shell
python3 main.py
```


> [!IMPORTANT]
> Ce projet est sous licence Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).<br>
> Vous pouvez copier, distribuer et modifier ce projet à condition que ce soit à des fins non commerciales et que vous me créditiez.<br>
> [Texte complet de la licence](LICENSE)<br>
> [Site officiel de la licence](https://creativecommons.org/licenses/by-nc/4.0/legalcode.fr)<br>