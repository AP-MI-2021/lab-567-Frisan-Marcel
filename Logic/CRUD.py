from Domain.Rezervare import creareRezervare, getId
from Exceptions.CustomExceptions import LogicError


def adaugaRezervare(id, nume, clasa, pret, checkin, lst):
    """
    :param id: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lst: list of sales
    :return: A list with all the sales
    """
    erori = ""
    try:
        id = int(id)
    except:
        erori += "Id-ul trebuie sa fie un numar! \n"
    try:
        pret = float(pret)
    except:
        erori += "Pretul trebuie sa fie ori int ori float! \n"
    if nume == "" :
        erori += "Numele nu poate fi vid \n"
    if clasa not in ["economy", "economy plus", "business"]:
        erori += "Clasa poate avea doar valori din ['economy', 'economy plus', 'business']"
    if checkin.lower() not in ["da","nu"]:
        erori += "Checkin trebuie sa fie 'da' sau 'nu' \n"
    if len(erori) != 0:
        raise LogicError(erori)
    rezervare = creareRezervare(id, nume, clasa, pret, checkin)
    return lst + [rezervare]


def getById(id, lst):
    """
    :param id: int
    :param list: lista cu rezervari
    :return: rezervarea cu id-ul dat, None daca nu exista lista cu id-ul dat
    """
    """ if len(lst) == 0:
        return None"""
    for rezervare in lst:
        if getId(rezervare) == id:
            return rezervare
    return None


def stergeRezervare(id, lst):
    """
    :param id: int
    :param list: lista de rezervari
    :return: lista cu toate rezervarile, mai putin cea cu id-ul dat
    """
    try:
        id = int(id)
    except:
        raise LogicError("Id-ul trebuie sa fie un numar!")
    if getById(id, lst) is None:
        raise LogicError("Nu exista rezervare cu id-ul dat!")
    return [rezervare for rezervare in lst if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lst):
    """
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin: string
    :param lst: lista rezervarilor
    :return: modified list
    """
    erori = ""
    try:
        id = int(id)
    except:
        erori += "Id-ul trebuie sa fie un numar! \n"
    try:
        pret = float(pret)
    except:
        erori += "Pretul trebuie sa fie ori int ori float! \n"
    if nume == "":
        erori += "Nume/Checkin nu au primit o valoare valida! \n"
    if clasa not in ["economy", "economy plus", "business"]:
        erori += "Clasa poate avea doar valori din ['economy', 'economy plus', 'business']"
    if checkin.lower() not in ["da","nu"]:
        erori += "Checkin trebuie sa fie 'da' sau 'nu' \n"
    if getById(id, lst) is None:
        erori += "Nu exista rezervare cu id-ul dat! \n"
    if len(erori) != 0:
        raise LogicError(erori)
    newList = []
    for rezervare in lst:
        if getId(rezervare) == id:
            rezervareNou = creareRezervare(id, nume, clasa, pret, checkin)
            newList.append(rezervareNou)
        else:
            newList.append(rezervare)
    return newList
