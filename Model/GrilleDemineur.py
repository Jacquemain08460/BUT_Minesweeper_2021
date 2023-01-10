# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True
def construireGrilleDemineur(nl : int, nc : int)-> list:
    if nl <=0 or nc <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nl} ou de colonnes {nc} est négatif ou nul.")
    if type(nl) != int or type(nc) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {type(nl)} ou de colonnes {type(nc)} n'est pas un entier.")
    grille =[]
    listTemp=[]
    for i in range(nl):
        for j in range(nc):
            listTemp += [construireCellule()]
        grille.append(listTemp)
        listTemp = []

    return grille
def getNbLignesGrilleDemineur(grille : list)-> int:
    if type_grille_demineur(grille) == False:
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n'est pas une grille.")
    nl = len(grille)
    return nl

def getNbColonnesGrilleDemineur(grille : list)-> int:
    if type_grille_demineur(grille) == False:
        raise TypeError(f"getNbColonnesGrilleDemineur : Le paramètre n'est pas une grille.")
    nc = len(grille[0])
    return nc

def isCoordonneeCorrecte(grille : list, coord : tuple)-> bool:
    contient = False
    if (type(coord[0]) != int) or (type(coord[1])!= int) or (type_grille_demineur(grille)==False):
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n'est pas du bon type.")
    nlGrille = getNbLignesGrilleDemineur(grille)
    ncGrille = getNbColonnesGrilleDemineur(grille)
    #print(ncGrille)
    if (nlGrille > coord[0]) and (ncGrille > coord[1]):
        contient = True
    return contient

def getCelluleGrilleDemineur(grille : list, coord : tuple)-> dict:
    if type_grille_demineur(grille)==False or type(coord[0])!=int or type(coord[1])!=int:
        raise TypeError(f"getCelluleGrilleDemineur : un des paramètres n'est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError(f"getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    dictCell = grille[coord[0]][coord[1]]
    return dictCell
def getContenuGrilleDemineur(grille : list, coord : tuple)->int:
    cellule = getCelluleGrilleDemineur(grille, coord)
    contenu = getContenuCellule(cellule)
    return contenu
def setContenuGrilleDemineur(grille : list, coord : tuple, contenu : int)-> None:
    cellule = getCelluleGrilleDemineur(grille, coord)
    setContenuCellule(cellule, contenu)
    return None
def isVisibleGrilleDemineur(grille : list, coord : tuple)->bool:
    cellule = getCelluleGrilleDemineur(grille, coord)
    isVisible = isVisibleCellule(cellule)
    return isVisible
def setVisibleGrilleDemineur(grille : list, coord : tuple, visible : bool)->None:
    cellule = getCelluleGrilleDemineur(grille, coord)
    setVisibleCellule(cellule, visible)
    return None
def contientMineGrilleDemineur(grille : list, coord : tuple)->bool:
    cellule = getCelluleGrilleDemineur(grille, coord)
    isMine = contientMineCellule(cellule)
    return isMine
def getCoordonneeVosinsGrilleDemineur(grille : list, coord : tuple)->list:
    if (type_grille_demineur(grille)==False) or type(coord[0])!=int or type(coord[1])!=int:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n'est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord)==False:
        raise IndexError("getCoordonneeVoisinGrilleDemineur : la coordonnée n'est pas dans la grille.")
    listCoord=[]
    coordTemp= (0,0)
    coordTemp[0]=coord[0]-1
    coordTemp[1]=coord[1]-1
    for i in range(0,3):
        if isCoordonneeCorrecte(grille, coordTemp) == True:
            c= getCelluleGrilleDemineur(grille, coordTemp)
            listCoord += [coordTemp]
        coordTemp[1]= coordTemp[1]+1
    coordTemp[0] += 1
    coordTemp[1] = coord[1]-1
    if isCoordonneeCorrecte(grille, coordTemp) == True:
        listCoord += [coordTemp]
    coordTemp[1] += 2
    if isCoordonneeCorrecte(grille, coordTemp) == True:
        listCoord += [coordTemp]
    coordTemp[0] += 1
    coordTemp[1] = coord[1]-1
    for i in range(0,3):
        if isCoordonneeCorrecte(grille, coordTemp) == True:
            listCoord += [coordTemp]
        coordTemp[1] += 1
    return listCoord