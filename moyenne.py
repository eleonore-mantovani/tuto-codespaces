"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    # docstrings en markdown
    L=0
    # Calcule la moyenne des valeurs.
    for val in (valeurs):
        L+= val
    #**Paramètres**
    #- `valeurs` : valeurs dont on veut calculer la moyenne

    #**Retour**
    #- la moyenne des valeurs
    return L/len(valeurs)
    #**Exceptions**
    #- `ValueError` : si la liste est vide
    if len(valeurs)==0:
        return L


    print("!! TODO : Compléter la fonction moyenne !!", end=" ")
    pass


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
