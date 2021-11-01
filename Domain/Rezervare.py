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
    return {"id":id,
            "nume": nume,
            "clasa": clasa,
            "pret": pret,
            "checkin": checkin
            }


def getId(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: id-ul rezervarii
    """
    return rezervare["id"]


def getNume(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: numele rezervarii
    """
    return rezervare["nume"]


def getClasa(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: clasa rezervarii
    """
    return rezervare["clasa"]


def getPret(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: the value of the sale
    """
    return rezervare["pret"]


def getCheckin(rezervare):
    """
    :param rezervare: dictionar care contine o rezervare
    :return: checkin-ul rezervarii
    """
    return rezervare["checkin"]

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
