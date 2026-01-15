# --------------------------- Search engine ---------------------------- #
# Lien du dépot : https://github.com/Pythacode/ecosia_simulator/         #
# Fichier contenant tout le code du moteur de recherche.                 #
# Crée par Titouan - https://github.com/Pythacode/                       #
# License :                                                              #
# ---------------------------------------------------------------------- #

import requests
import json

def search(query:str, max_result=10, lang="fr") -> list:
    """
    Recherche `query` grace à l'API de search1API
    https://www.search1api.com/#features
    
    :param query: Chaine de caractère à rechercher
    :type query: str
    :param max_result: Nombre maximum de résultats attendus.
    :type max_result: int
    :param lang: Langue de la recherche
    :type lang: str
    :return: Une liste de dictionnaires qui comportent les informations de chaques résultats
    :rtype: list
    """

    API_URL = "https://api.search1api.com/search"
    
    # Paramètre de la recherche
    data = {
        "query": query,
        "max_results": max_result,
        "crawl_results": 2,  
        "image": False,
        "language": lang
    }

    # Headers de la requete
    headers = {
        "Content-Type": "application/json" # Réponse attendus en JSON
    }

    # Réponse de la requete
    response = requests.post(
        API_URL,
        headers=headers,
        json=data
    )

    results = response.json().get('results')
    exploit_result = [{
            "title" : r.get('title'),
            "link" : r.get('link'),
            "snippet" : r.get('snippet')
        } for r in results] # Suprime les informations inutiles à notre usage

    return exploit_result
