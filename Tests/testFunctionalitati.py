from Logic.AlteFunctionalitati import *
from Domain.Rezervare import *
from Logic.CRUD import adaugaRezervare

def testUpgradeClasaByNume():
    lst = []
    lst = adaugaRezervare(1, "paul", "economy", 44, "da", lst)
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "nu", lst)
    lst = adaugaRezervare(3, "paul", "business", 2, "da", lst)
    lst = adaugaRezervare(4, "mircea", "economy", 44, "da", lst)

    lst = upgradeClasaByNume("paul", lst)

    assert getClasa(lst[0]) == "economy plus"
    assert getClasa(lst[1]) == "business"
    assert getClasa(lst[2]) == "business"
    assert getClasa(lst[3]) == "economy"

def testReducerePretLaCheckinFacut():
    lst = []
    lst = adaugaRezervare(1, "paul", "economy", 44, "nu", lst)
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)
    lst = adaugaRezervare(3, "paul", "business", 2, "da", lst)
    lst = adaugaRezervare(4, "mircea", "economy", 44, "da", lst)

    lst = reducerePretLaCheckinFacut(10, lst)

    assert getPret(lst[0]) == 44.0
    assert getPret(lst[1]) == 29.7
    assert getPret(lst[2]) == 1.8
    assert getPret(lst[3]) == 39.6