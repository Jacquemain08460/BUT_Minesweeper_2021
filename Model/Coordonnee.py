# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0
def construireCoordonnee(num_li:int, num_co:int)->tuple:
    if type(num_li) != int or type(num_co) != int:
        raise TypeError(f"construireCoordonnee: Le numéro de ligne {type(num_li)} ou le numéro de colonne {type(num_co)} ne sont pas des entiers.")
    if num_li <0 or num_co < 0:
        raise ValueError(f"construireCoordonne : Le numéro de ligne {num_li} ou de colonne {num_co} ne sont pas positifs.")
    lico = (num_li,num_co)
    return lico
def getLigneCoordonne(lico:tuple)->int:
    if type_coordonnee(lico) == False:
        raise TypeError(f"getLigneCoordonne : Le paramètre n'est pas une coordonnée.")
    num_li = lico[0]
    return num_li
def getColonneCoordonnee(lico:tuple)->int:
    if type_coordonnee(lico) == False :
        raise TypeError(f"getColonneCoordonnee : Le paramètre n'est pas une coordonnee.")
    num_co = lico[1]
    return num_co

