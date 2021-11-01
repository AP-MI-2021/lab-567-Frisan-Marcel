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