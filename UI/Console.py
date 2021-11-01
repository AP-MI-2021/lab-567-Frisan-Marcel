from Domain.Rezervare import toString
from Exceptions.CustomExceptions import DomainError, LogicError
from Logic.CRUD import *
from Logic.AlteFunctionalitati import reducerePretLaCheckinFacut, upgradeClasaByNume
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
    print("c. Afiseaza rezervarile")
    print("x. Exit")


def uiAdaugaRezervare(lst):
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
        return adaugaRezervare(id, nume, clasa, pret, checkin, lst)
    except LogicError as le:
        print(f"Error: {le}")
        return lst
    


def uiStergeRezervare(lst):
    """
    sterge o rezervare din lista
    :param lst: lista rezervarilor
    :return: updated list
    """
    try:
        id = input("Id: ")
        return stergeRezervare(id, lst)
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def uiModificaRezervare(lst):
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
        return modificaRezervare(id, nume, clasa, pret, checkin, lst)
    except LogicError as le:
        print(f"Error: {le}")
        return lst
    
def uiUpgradeClasaByNume(lst):
    """
    upgradeaza clasa tuturor rezervarilor facute pe un nume x, 
        unde x este citit de la tastatura
    :param lst: lista rezervarilor
    """
    try:
        nume = input("Nume cautat: ")
        return upgradeClasaByNume(nume, lst)
    except LogicError as le:
        print(f"Error: {le}")
        return lst

def uiReducerePretLaCheckinFacut(lst):
    """
    aplica o reducere procentuala citita de la tastatura rezervarilor 
        care au checkin facut
    :param lst: lista rezervarilor
    :return: lista actualizata
    """
    try:
        reducere = input("Reducere procentuala aplicata: ")
        return reducerePretLaCheckinFacut(reducere, lst)
    except LogicError as le:
        print(f"Error: {le}")
        return lst


def runMenu(lst):
    """
    ruleaza loop-ul programului
    :param lst: lista rezervarilor
    """
    while True:
        printMenu()
        optiune = input("Option: ")
        if optiune == "1":
            lst = uiAdaugaRezervare(lst)
        elif optiune == "2":
            lst = uiStergeRezervare(lst)
        elif optiune == "3":
            lst = uiModificaRezervare(lst)
        elif optiune == "4":
            lst = uiUpgradeClasaByNume(lst)
        elif optiune == "5":
            lst = uiReducerePretLaCheckinFacut(lst)
        elif optiune == "x":
            break
        elif optiune == "c":
            showAll(lst)
        else:
            print("Invalid option! ")