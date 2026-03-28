import sqlite3
import os

dbPath = os.sep.join([os.path.split(__file__)[0], # Obtient le chemin absolus de `game.py`
                        '..', # Remonte d'un répertoir (Répertoir source)
                        'data',
                        'ecopixel.db'
                    ])

filePath = os.sep.join([os.path.split(__file__)[0], "install.sh"])

with open(filePath, "r", encoding="utf-8") as f:
    sql = f.read()

with sqlite3.connect(dbPath) as conn:
    conn.executescript(sql)
    print(f"✅ '{filePath}' exécuté avec succès sur '{dbPath}'")
