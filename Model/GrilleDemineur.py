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
    if (type(coord[0]) != int) or (type(coord[1]) != int) or (type_grille_demineur(grille)==False):
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n'est pas du bon type.")
    nlGrille = getNbLignesGrilleDemineur(grille)
    ncGrille = getNbColonnesGrilleDemineur(grille)
    if (nlGrille > coord[0]) and (ncGrille > coord[1]) and coord[0] >= 0 and coord[1] >= 0:
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

def getCoordonneeVoisinsGrilleDemineur(grille : list, coord : tuple)->list:
    if (type_grille_demineur(grille)==False) or type(coord[0])!=int or type(coord[1])!=int:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n'est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord)==False:
        raise IndexError("getCoordonneeVoisinGrilleDemineur : la coordonnée n'est pas dans la grille.")
    listCoord=[]
    if isCoordonneeCorrecte(grille,(coord[0]-1,coord[1]-1)) == True:
        listCoord += [(coord[0]-1,coord[1]-1)]
    if isCoordonneeCorrecte(grille,(coord[0]-1,coord[1])) == True:
        listCoord += [(coord[0]-1,coord[1])]
    if isCoordonneeCorrecte(grille,(coord[0]-1,coord[1]+1)) == True:
        listCoord += [(coord[0]-1,coord[1]+1)]
    if isCoordonneeCorrecte(grille,(coord[0],coord[1]-1)) == True:
        listCoord += [(coord[0],coord[1]-1)]
    if isCoordonneeCorrecte(grille, (coord[0],coord[1]+1)) == True:
        listCoord += [(coord[0],coord[1]+1)]
    if isCoordonneeCorrecte(grille,(coord[0]+1,coord[1]-1)) == True:
        listCoord += [(coord[0]+1,coord[1]-1)]
    if isCoordonneeCorrecte(grille,(coord[0]+1,coord[1])) == True:
        listCoord += [(coord[0]+1,coord[1])]
    if isCoordonneeCorrecte(grille,(coord[0]+1,coord[1]+1)) == True:
        listCoord += [(coord[0]+1,coord[1]+1)]
    return listCoord

def placerMinesGrilleDemineur(grille : list, nb : int, coord : tuple)->None:
    if nb <=0 or (nb >= (getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille))):
        raise ValueError("placerMinesGrillesDemineur : Nombre de bombes à placer incorrect.")
    if isCoordonneeCorrecte(grille,coord) == False:
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n'est pas dans la grille.")
    while nb >0:
        coordTemp1 = randint(0, len(grille)-1)
        coordTemp2 = randint(0, len(grille[0])-1)
        coordTempTuple = (coordTemp1, coordTemp2)
        while (coordTempTuple == coord) or (contientMineGrilleDemineur(grille,coordTempTuple) == True) or (isCoordonneeCorrecte(grille,coordTempTuple) == False):
            coordTemp1 = randint(0, len(grille)-1)
            coordTemp2 = randint(0, len(grille[0])-1)
            coordTempTuple = (coordTemp1, coordTemp2)
        cellule = getCelluleGrilleDemineur(grille,coordTempTuple)
        if isCoordonneeCorrecte(grille, coordTempTuple)==True:
            setContenuCellule(cellule, const.ID_MINE)
            nb = nb-1
    compterMinesVoisinesGrilleDemineur(grille)
    return None
def compterMinesVoisinesGrilleDemineur(grille : list)->None:
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            compteMine = 0
            cellTemp = getCelluleGrilleDemineur(grille, (i,j))
            if getContenuCellule(cellTemp) != const.ID_MINE:
                listCoordTemp = getCoordonneeVoisinsGrilleDemineur(grille,(i,j))
                for p in range(len(listCoordTemp)):
                    if getContenuCellule(getCelluleGrilleDemineur(grille,listCoordTemp[p])) == const.ID_MINE:
                        compteMine = compteMine + 1
                setContenuCellule(cellTemp,compteMine)

    return None
def getNbMinesGrilleDemineur(grille : list)->int:
    if type_grille_demineur(grille) == False:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n'est pas une grille.")
    compteMine = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i,j))
            if contientMineCellule(cellule) == True:
                compteMine += 1
    return compteMine

def getAnnotationGrilleDemineur(grille : list, coord : tuple)-> str:
    cellule = getCelluleGrilleDemineur(grille, coord)
    annot = getAnnotationCellule(cellule)
    return annot

def getMinesRestantesGrilleDemineur(grille : list)->int:
    nbMine = getNbMinesGrilleDemineur(grille)
    nbFlag = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            coord = (i,j)
            cellule = getCelluleGrilleDemineur(grille, coord)
            if cellule[const.ANNOTATION] == const.FLAG:
                nbFlag += 1
    nbRestant = nbMine - nbFlag
    return nbRestant

def gagneGrilleDemineur(grille : list)-> bool:
    gagne = False
    comptePoint = 0
    iter = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i,j))
            contenu = getContenuCellule(cellule)
            if contientMineCellule(cellule) == True and isVisibleCellule(cellule) == False and getAnnotationCellule(cellule) == const.FLAG:
                comptePoint += 1
            elif contenu != -1 and isVisibleCellule(cellule) == True:
                comptePoint += 1
            iter += 1
    if comptePoint == (len(grille)*len(grille[0])):
        gagne = True
    return gagne

def perduGrilleDemineur(grille : list)-> bool:
    perdu = False
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i,j))
            contenu = getContenuCellule(cellule)
            visible = isVisibleCellule(cellule)
            if contenu == -1 and visible == True:
                perdu = True
    return perdu

def reinitialiserGrilleDemineur(grille : list)-> None:
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i,j))
            reinitialiserCellule(cellule)
    return None

def decouvrirGrilleDemineur(grille : list, coord : tuple, setBase = set())->set:
    setBase = set()
    cellule = getCelluleGrilleDemineur(grille, coord)
    setVisibleCellule(cellule, True)
    setBase.add(coord)
    if getContenuCellule(cellule) == 0:
        listVoisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        for i in range(len(listVoisins)):
            celluleTemp= getCelluleGrilleDemineur(grille, listVoisins[i])
            if getContenuCellule(celluleTemp)  == 0 and isVisibleCellule(celluleTemp) == False:
                iter = decouvrirGrilleDemineur(grille, listVoisins[i])
                for j in iter:
                    setBase.add(j)
    return setBase

def simplifierGrilleDemineur(grille, coord : tuple)-> set:
    ensemble = set()
    compteFlag = 0
    cellule = getCelluleGrilleDemineur(grille, coord)
    if isVisibleCellule(cellule) == True:
        ensembe.add(coord)
        listVoisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        for i in range(len(listVoisins)):
            celluleTemp = getCelluleGrilleDemineur(grille, listVoisins[i])
            if getAnnotationGrilleDemineur(grille, listVoisins[i]) == const.FLAG:
                compteFlag += 1
        if compteFlag == getContenuCellule(celluleTemp):
            for i in range(len(listVoisins)):
                getCelluleGrilleDemineur(grille, listVoisins[i])[const.ANNOTATION] = const.FLAG
                celluleTemp = getCelluleGrilleDemineur(grille, listVoisin[i])
                if isVisibleCellule(celluleTemp) == False and celluleTemp[const.ANNOTATION] != const.FLAG:
                    setVisibleCellule(celluleTemp,True)
                    boucle = simplifierGrilleDemineur(grille, listVoisins[i])
                    for j in range(boucle):
                        ensemble.add(boucle[j])
    return ensemble

def ajouterFlagGrilleDemineur(grille : list, coord : tuple)->set:
    listVoisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    compte = 0
    ensemble = set()
    for i in range(len(listVoisins)):
        celluleTemp = getCelluleGrilleDemineur(grille, listVoisins[i])
        if isVisibleCellule(celluleTemp) == False:
            compte += 1
    cellule = getCelluleGrilleDemineur(grille, coord)
    if getContenuCellule(cellule) == compte:
        for i in range(len(listVoisins)):
            cellultTemp = getCelluleGrilleDemineur(grille, listVoisins[i])
            if isVisibleCellule(celluleTemp) == False:
                celluleTemp[const.ANNOTATION] = const.FLAG
                ensemble.add(listVoisins[i])
    return ensemble

def simplifierToutDemineur(grille : list)->tuple:
    setVisible = set()
    setVisibleTemp = set()
    setFlag = set()
    setFlagTemp = set()
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            celluleTemp = getCelluleGrilleDemineur(grille, (i,j))
            if isVisibleCellule(celluleTemp) == True:
                setVisibleTemp = simplifierGrilleDemineur(grille, (i,j))
                for k in range(len(setVisibleTemp)):
                    if setVisibleTemp[k] not in setVisible:
                        setVisible.add(setVisi)
                setVisibleTemp = set()
                setFlagTemp = ajouterFlagGrilleDemineur(grille, (i,j))
                for k in range(len(setFlagTemp)):
                    if setFlagTemp[k] not in setFlag:
                        setFlag.add(setFlagTemp[k])
                setFlagTemp = set()
    return ((setVisible), (setFlag))
