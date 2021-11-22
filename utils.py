from Domain.Rezervare import toString

def getRunMethod():
    """
    citeste de la tastatura un string si accepta doar "commands" sau "menu"
    """
    runMethod = ""
    while runMethod.lower() not in ["commands", "menu"]:
        print("Programul poate rula cu menu sau prin comenzi")
        runMethod = input("Introduceti metoda de rulare a programului (menu/commands): ")
    
    return runMethod.lower()


def showAll(lst):
    """
    afiseaza lista de rezervari
    :param lst: lista rezervarilor
    """
    if len(lst) == 0:
        print("Nu exista nicio rezervare in db!")
        return
    try:
        for rezervare in lst:
            print(toString(rezervare))
    except:
        print("Error: Nicio rezervare nu a fost adaugata inca!")
