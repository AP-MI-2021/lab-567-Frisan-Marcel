from Exceptions.CustomExceptions import LogicError
from Domain.Rezervare import *

def upgradeClasaByNume(nume, lst):
    """
    mareste clasa tuturor rezervarilor cu nume=param:nume
    :param nume: string
    :param lst: list
    return: lista actualizata
    """
    if nume == "":
        raise LogicError("Numele introdus nu contine o valoare valida!")
    newList = []
    for rezervare in lst:
        if nume == getNume(rezervare):
            if getClasa(rezervare) == "economy":
                clasaNoua = "economy plus"
            else:
                clasaNoua = "business"
            rezervareNoua = creareRezervare(
                getId(rezervare),
                nume,
                clasaNoua,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            newList.append(rezervareNoua)
        else:
            newList.append(rezervare)
    return newList

def reducerePretLaCheckinFacut(procent, lst):
    """
    aplica o reducere de procent% tuturor rezervarilor cu checkin == "da"
    :param procent: string
    :param lst: list
    return: lista actualizata
    """
    try:
        procent = int(procent)
    except:
        raise LogicError("Procentul trebuie sa fie un numar!")
    if procent > 100:
        raise LogicError("Procentul trebuie sa fie <= 100 !")
    newList = []
    for rezervare in lst:
        if getCheckin(rezervare).lower() == "da":
            pretNou = getPret(rezervare)*(100-procent)/100
            rezervareNoua = creareRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                pretNou,
                getCheckin(rezervare)
            )
            newList.append(rezervareNoua)
        else:
            newList.append(rezervare)
    return newList

def pretMaxPerClasa(lst):
    """
    determina cel mai mare pret pentru fiecare clasa 
    :param lst: list
    return: dict ce contine ca si chei clasele, iar la valori are cel mai mare pret pentru clasa respectiva
    """
    if len(lst) == 0:
        raise LogicError("Trebuie sa adaugati mai intai rezervari!")
    rezultat = {}
    for rezervare in lst:
        clasa = getClasa(rezervare)
        pret = getPret(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret

    return rezultat

def returnPret(rezervare):
    return getPret(rezervare)

def ordonareDescDupaPret(lst):
    """
    ordoneaza lista descrescator dupa pret
    :param lst: list
    return: lista ordonata
    """
    return sorted(lst, key=returnPret, reverse=True)

def totalPreturiPerNume(lst):
    """
    calculeaza totalul preturilor pentru fiecare nume
    :param lst: list
    return: dict ce contine ca si chei numele, iar la valori totalul preturilor pentru acel nume
    """
    if len(lst) == 0:
        raise LogicError("Trebuie sa adaugati mai intai rezervari")
    rezultat = {}
    for rezervare in lst:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] += pret
        else:
            rezultat[nume] = pret
    return rezultat