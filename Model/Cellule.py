# Model/Cellule.py
#
import constantly

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
def construireCellule(contenu: int =0, visible: bool =False)->dict:
    if isContenuCorrect(contenu) == False:
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct.")
    elif type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n'est pas un booléen.")
    else:
        dictCell = {const.CONTENU : contenu, const.VISIBLE : visible, const.ANNOTATION : None}
    return dictCell

def getContenuCellule(dictCell : dict)-> int:
    if type_cellule(dictCell) == False:
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    else:
        contenu = dictCell[const.CONTENU]
    return contenu

def isVisibleCellule(dictCell : dict)-> bool:
    if type_cellule(dictCell) == False:
        raise TypeError(f"isVisibleCellule : Le paramètre n'est pas une cellule.")
    visible = dictCell[const.VISIBLE]
    return visible

def setContenuCellule(dictCell : dict, contenu: int)-> None:
    if type_cellule(dictCell) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n'est pas une cellule.")
    elif type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n'est pas un entier.")
    elif isContenuCorrect(contenu)==False:
        raise ValueError(f"setContenuCellule: la valeur du contenu {contenu} n'est pas correcte.")
    else:
        dictCell[const.CONTENU]=contenu
    return None

def setVisibleCellule(dictCell : dict, visible : bool)->None:
    if type_cellule(dictCell) == False:
        raise TypeError(f"setVisibleCellule : Le premier paramètre n'est pas une cellule.")
    elif type(visible) != bool:
        raise TypeError(f"setVisibleCellule : Le second paramètre n'est pas un booléen.")
    else:
        dictCell[const.VISIBLE]=visible
    return None
def contientMineCellule(dictCell : dict)-> bool:
    if type_cellule(dictCell) == False:
        raise TypeError(f"contientMineCellule: Le paramètre n'est pas une cellule.")
    elif dictCell[const.CONTENU]==const.ID_MINE:
        isMine = True
    else:
        isMine = False
    return isMine

def isAnnotationCorrecte(annot : str)->bool:
    isAnnotCorrect = False
    if annot == None or annot == const.DOUTE or annot == const.FLAG:
        isAnnotCorrect = True
    return isAnnotCorrect

def getAnnotationCellule(cellule : dict)-> str:
    if type_cellule(cellule) == False:
        raise TypeError(f"getAnnotationCellule : le paramètre {cellule} n'est pas une cellule")
    if const.ANNOTATION not in cellule:
        return None
    else:
        annot = cellule[const.ANNOTATION]
        return annot

def changeAnnotationCellule(cellule : dict)->None:
    if type_cellule(cellule) == False:
        raise TypeError("changeAnnotationCellule : le paramètre n'est pas une cellule.")
    if cellule[const.ANNOTATION] == None:
        cellule[const.ANNOTATION] = const.FLAG
    elif cellule[const.ANNOTATION] == const.FLAG:
        cellule[const.ANNOTATION] = const.DOUTE
    elif cellule[const.ANNOTATION] == const.DOUTE:
        cellule[const.ANNOTATION] = None
    return None

