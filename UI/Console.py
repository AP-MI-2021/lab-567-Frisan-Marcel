from Domain.Rezervare import toString
from Logic.CRUD import *

def printMenu():
    """
    Afiseaza meniul
    """
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    # print("4. ")
    print("c. Afiseaza rezervarile")
    print("x. Exit")


def uiAdaugaRezervare(lst):
    """
    :param lst: lista rezervarilor
    :return: lista veche + rezervarea noua
    """
    id = int(input("Id: "))
    nume = input("Nume: ")
    clasa = input("Clasa: ")
    pret = float(input("Pret: "))
    checkin = input("Checkin: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lst)


def uiStergeRezervare(lst):
    """
    sterge o rezervare din lista
    :param lst: lista rezervarilor
    :return: updated list
    """
    id = int(input("Id: "))
    return stergeRezervare(id, lst)


def uiModificaRezervare(lst):
    """
    modifica o rezervare din lista
    :param lst: lista rezervarilor
    :return: lista actualizata
    """
    id = int(input("Id: "))
    nume = input("Nume nou: ")
    clasa = input("Clasa noua: : ")
    pret = float(input("Pret nou: "))
    checkin = input("Checkin nou: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lst)


def showAll(lst):
    """
    afiseaza lista de rezervari
    :param lst: lista rezervarilor
    """
    for rezervare in lst:
        print(toString(rezervare))


def runMenu(lst):
    """
    ruleaza loop-ul programului
    :param lst: lista rezervarilor
    """
    while True:
        printMenu()
        showAll(lst)
        optiune = input("Option: ")
        if optiune == "1":
            lst = uiAdaugaRezervare(lst)
        elif optiune == "2":
            lst = uiStergeRezervare(lst)
        elif optiune == "3":
            lst = uiModificaRezervare(lst)
        elif optiune == "x":
            break
        elif optiune == "c":
            showAll(lst)
        else:
            print("Invalid option! ")