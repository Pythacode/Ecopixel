# <img src="/data/image/icon/logo.png" alt="Logo du jeu" width="50" height="50"> ecosia_simulator

Un jeu où l'on peut planter des arbres en achetant des pousses grâce au crédits que l'on gagnerait en faisant des recherches sur le web

## Sommaire

- [Installation](#installation)
- [Lancement](#lancement)
    - [Avec venv](#avec-venv)
    - [Sans venv](#sans-venv)

## Installation

> [!TIP]
> Dans ce README, nous utiliserons les commandes `python3` et `pip`. Cepeandant, suivant votre installation, vous devriez peut-être utiliser `python` et `python3 -m pip` à la place.

## Lancement

### Avec venv

[Documentation officiel](https://docs.python.org/3/library/venv.html "Documentation officiel venv")

Pour commencer, if faut créer un venv avec la commande suivante en étant dans le répertoiree racine du projet:
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
    | cmd.exe | `C:\> venv\Scripts\activate.bat` |
    | PowerShell | `PS C:\> venv\Scripts\Activate.ps1` |

Ensuite, installez les dépendences avec :

```
pip install -r requirements.txt
```

Enfin, lancez simplement le projet avec la commande :

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
> Ce projet est sous licence GNU 3v+ pour le code et Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). pour le texte<br>
> Plus d'information :' [Fichier LICENSE](LICENSE)<br>
> [Site officiel de la licence GNU v3+](https://www.gnu.org/licenses/gpl-3.0.fr.html)<br>
> [Site officiel de la licence CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/legalcode.fr)
