def creareRezervare(id, nume, clasa, pret, checkin):
    """
    creaza o noua rezervare
    :param id: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar cu rezervarea creata
    """
    return (id, nume, clasa, pret, checkin)


def getId(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: id-ul rezervarii
    """
    return rezervare[0]


def getNume(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: numele rezervarii
    """
    return rezervare[1]


def getClasa(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: clasa rezervarii
    """
    return rezervare[2]


def getPret(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: the value of the sale
    """
    return rezervare[3]


def getCheckin(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: checkin-ul rezervarii
    """
    return rezervare[4]


def toString(rezervare):
    """
    :param sale: dictionar care contine o rezervare
    :return: rezervarea foramtata in string
    """
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
