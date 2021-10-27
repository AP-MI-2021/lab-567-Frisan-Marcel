from Domain.Rezervare import *
from Logic.CRUD import *

def testCreazaRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "Clasa", 1.9, "Da", lst)

    assert len(lst) == 1
    assert getId(getById(1, lst)) == 1
    assert getNume(getById(1, lst)) == "Nume"
    assert getClasa(getById(1, lst)) == "Clasa"
    assert getPret(getById(1, lst)) == 1.9
    assert getCheckin(getById(1, lst)) == "Da"

def testModificaRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "Clasa", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "Clasa2", 3.0, "Nu", lst)

    lst = modificaRezervare(1, "newNume", "newClasa", 2.5, "Nu", lst)

    assert len(lst) == 2
    assert getId(getById(1, lst)) == 1
    assert getNume(getById(1, lst)) == "newNume"
    assert getClasa(getById(1, lst)) == "newClasa"
    assert getPret(getById(1, lst)) == 2.5
    assert getCheckin(getById(1, lst)) == "Nu"

def testStergeRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "Clasa", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "Clasa2", 3.0, "Nu", lst)

    lst = stergeRezervare(1, lst)
    assert len(lst) == 1

def testGetById():
    lst = []
    lst = adaugaRezervare(1, "Nume", "Clasa", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "Clasa2", 3.0, "Nu", lst)

    assert getById(1, lst) == (1, "Nume", "Clasa", 1.9, "Da")