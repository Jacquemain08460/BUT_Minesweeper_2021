# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)
def isContenuCorrect(n:int)->bool:
    contenuCorrect=False
    valeurPoss = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    u=0
    if type(n) != int:
        return False
    else:
        while not contenuCorrect and u <9:
            if valeurPoss[u] == n:
                contenuCorrect = True
            u += 1
        if n == const.ID_MINE:
            contenuCorrect = True
        return contenuCorrect

