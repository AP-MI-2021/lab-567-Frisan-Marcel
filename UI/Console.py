from Domain.Rezervare import toString
from Exceptions.CustomExceptions import DomainError, LogicError
from Logic.CRUD import *
from Logic.AlteFunctionalitati import reducerePretLaCheckinFacut, upgradeClasaByNume, pretMaxPerClasa, ordonareDescDupaPret, totalPreturiPerNume
from utils import showAll


def printMenu():
    """
    Afiseaza meniul
    """
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Upgradeaza clasa rezervarilor care sunt facute pe un nume citit")
    print("5. Aplica un procent citit pentru rezervarile care au checkin facut")
    print("6. Afisare pret maxim pentru fiecare clasa")
    print("7. Ordonare descrescatoare dupa pret")
    print("8. Afiseaza totalul pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("c. Afiseaza rezervarile")
    print("x. Exit")


def uiAdaugaRezervare(lst, undoList, redoList):
    """
    :param lst: lista rezervarilor
    :return: lista veche + rezervarea noua
    """
    try:
        id = input("Id: ")
        nume = input("Nume: ")
        clasa = input("Clasa: ")
        pret = input("Pret: ")
        checkin = input("Checkin: ")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lst)
        undoList.append(lst)
        redoList.clear()
        return rezultat
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiStergeRezervare(lst, undoList, redoList):
    """
    sterge o rezervare din lista
    :param lst: lista rezervarilor
    :return: updated list
    """
    try:
        id = input("Id: ")
        rezultat = stergeRezervare(id, lst)
        undoList.append(lst)
        redoList.clear()
        return rezultat
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiModificaRezervare(lst, undoList, redoList):
    """
    modifica o rezervare din lista
    :param lst: lista rezervarilor
    :return: lista actualizata
    """
    try:
        id = input("Id: ")
        nume = input("Nume nou: ")
        clasa = input("Clasa noua: : ")
        pret = input("Pret nou: ")
        checkin = input("Checkin nou: ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lst)
        undoList.append(lst)
        redoList.clear()
        return rezultat
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiUpgradeClasaByNume(lst, undoList, redoList):
    """
    upgradeaza clasa tuturor rezervarilor facute pe un nume x, 
        unde x este citit de la tastatura
    :param lst: lista rezervarilor
    """
    try:
        nume = input("Nume cautat: ")
        rezultat = upgradeClasaByNume(nume, lst)
        undoList.append(lst)
        redoList.clear()
        return rezultat
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiReducerePretLaCheckinFacut(lst, undoList, redoList):
    """
    aplica o reducere procentuala citita de la tastatura rezervarilor 
        care au checkin facut
    :param lst: lista rezervarilor
    :return: lista actualizata
    """
    try:
        reducere = input("Reducere procentuala aplicata: ")
        rezultat = reducerePretLaCheckinFacut(reducere, lst)
        undoList.append(lst)
        redoList.clear()
        return rezultat
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiPretMaxPerClasa(lst):
    """
    determina cel mai mare pret pentru fiecare clasa 
    :param lst: list
    return: dict ce contine ca si chei clasele, iar la valori are cel mai mare pret pentru clasa respectiva
    """
    try:
        rezultat = pretMaxPerClasa(lst)
        for clasa in rezultat:
            print(f'{clasa}: {rezultat[clasa]}')
    except LogicError as le:
        print(f"Error: {le}")


def uiOrdonareDescDupaPret(lst, undoList, redoList):
    """
    ordoneaza lista descrescator dupa pret
    :param lst: list
    return: lista ordonata
    """
    listaNoua = ordonareDescDupaPret(lst)
    undoList.append(lst)
    redoList.clear()
    return listaNoua


def uiTotalPreturiPerNume(lst):
    """
    Afiseaza fiecare nume din lista si suma preturilor pentru acestea
    :param lst: lista
    """
    rezultat = totalPreturiPerNume(lst)
    for nume in rezultat:
        print(f"{nume}: {rezultat[nume]}")


def runMenu(lst):
    """
    ruleaza loop-ul programului
    :param lst: lista rezervarilor
    """
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Option: ")
        if optiune == "1":
            lst = uiAdaugaRezervare(lst, undoList, redoList)
        elif optiune == "2":
            lst = uiStergeRezervare(lst, undoList, redoList)
        elif optiune == "3":
            lst = uiModificaRezervare(lst, undoList, redoList)
        elif optiune == "4":
            lst = uiUpgradeClasaByNume(lst, undoList, redoList)
        elif optiune == "5":
            lst = uiReducerePretLaCheckinFacut(lst, undoList, redoList)
        elif optiune == "6":
            uiPretMaxPerClasa(lst)
        elif optiune == "7":
            lst = uiOrdonareDescDupaPret(lst, undoList, redoList)
        elif optiune == "8":
            uiTotalPreturiPerNume(lst)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lst)
                lst = undoList.pop()
            else:
                print("Nu se poate face undo")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lst)
                lst = redoList.pop()
            else:
                print("Nu se poate face redo")
        elif optiune == "x":
            break
        elif optiune == "c":
            showAll(lst)
        else:
            print("Invalid option! ")
