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


def testPretMaxPerClasa():
    lst = []
    lst = adaugaRezervare(1, "paul", "economy", 44, "nu", lst)
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)
    lst = adaugaRezervare(3, "paul", "business", 2, "da", lst)
    lst = adaugaRezervare(4, "mircea", "economy", 1, "da", lst)
    lst = adaugaRezervare(4, "ana", "economy plus", 50, "da", lst)

    rezultat = pretMaxPerClasa(lst)
    assert(rezultat == {'economy': 44, 'economy plus': 50, 'business': 2})


def testOrdonareDescDupaPret():
    lst = []
    lst = adaugaRezervare(1, "paul", "economy", 4, "nu", lst)
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)
    rez = ordonareDescDupaPret(lst)
    assert rez == [{'id': 2, 'nume': 'paul', 'clasa': 'economy plus', 'pret': 33.0, 'checkin': 'da'}, {
        'id': 1, 'nume': 'paul', 'clasa': 'economy', 'pret': 4.0, 'checkin': 'nu'}]


def TestTotalPreturiPerNume():
    lst = []
    lst = adaugaRezervare(1, "paul", "economy", 44, "nu", lst)
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)
    lst = adaugaRezervare(3, "mircea", "business", 2, "da", lst)
    lst = adaugaRezervare(4, "mircea", "economy", 1, "da", lst)
    lst = adaugaRezervare(4, "ana", "economy plus", 50, "da", lst)

    rez = totalPreturiPerNume(lst)
    assert rez == {'paul': 77.0, 'mircea': 3.0, 'ana': 50.0}


def testUndoRedo():
    undoList = []
    redoList = []
    lst = []

    # se adauga 3 valori initiale

    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(1, "paul", "economy", 44, "nu", lst)

    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)

    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(3, "mircea", "business", 2, "da", lst)

    # 3x undo

    redoList.append(lst)
    lst = undoList.pop()
    assert(len(lst) == 2)

    redoList.append(lst)
    lst = undoList.pop()
    assert(len(lst) == 1)

    redoList.append(lst)
    lst = undoList.pop()
    assert(len(lst) == 0)

    # adaugam iar rezervari
    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(1, "paul", "economy", 44, "nu", lst)

    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(2, "paul", "economy plus", 33, "da", lst)

    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(3, "mircea", "business", 2, "da", lst)


    if(len(redoList) > 0):
        lst = redoList.pop()
    assert(lst == [{'id': 1, 'nume': 'paul', 'clasa': 'economy', 'pret': 44.0, 'checkin': 'nu'}, {'id': 2, 'nume': 'paul',
           'clasa': 'economy plus', 'pret': 33.0, 'checkin': 'da'}, {'id': 3, 'nume': 'mircea', 'clasa': 'business', 'pret': 2.0, 'checkin': 'da'}])


    redoList.append(lst)
    lst = undoList.pop()
    redoList.append(lst)
    lst = undoList.pop()

    assert(len(lst) == 1)

    undoList.append(lst)
    lst = redoList.pop()

    assert(len(lst) == 2)

    undoList.append(lst)
    lst = redoList.pop()

    assert(len(lst) == 3)

    redoList.append(lst)
    lst = undoList.pop()
    redoList.append(lst)
    lst = undoList.pop()

    assert(len(lst) == 1)
    undoList.append(lst)
    redoList.clear()
    lst = adaugaRezervare(1, "ana", "economy", 3, "da", lst)

    if (len(redoList) > 0):
        undoList.append(lst)
        lst = redoList.pop()
        assert (len(lst) == 2)

    redoList.append(lst)
    lst = undoList.pop()
    assert(len(lst) == 1)

    redoList.append(lst)
    lst = undoList.pop()
    assert (len(lst) == 0)

    if (len(redoList) > 0):
        undoList.append(lst)
        lst = redoList.pop()
    if (len(redoList) > 0):
        undoList.append(lst)
        lst = redoList.pop()
    assert (len(lst) == 2)