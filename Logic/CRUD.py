from Domain.Rezervare import creareRezervare, getId


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
    rezervare = creareRezervare(id, nume, clasa, pret, checkin)
    return lst + [rezervare]


def getById(id, lst):
    """
    :param id: int
    :param list: lista cu rezervari
    :return: rezervarea cu id-ul dat, None daca nu exista lista cu id-ul dat
    """
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
    return [rezervare for rezervare in lst if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lst):
    """
    :param id: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lst: lista rezervarilor
    :return: modified list
    """
    newList = []
    for rezervare in lst:
        if getId(rezervare) == id:
            rezervareNou = creareRezervare(id, nume, clasa, pret, checkin)
            newList.append(rezervareNou)
        else:
            newList.append(rezervare)
    return newList
