from Domain.Rezervare import *
from Logic.CRUD import *

def testCreazaRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "economy", 1.9, "Da", lst)

    assert len(lst) == 1
    assert getId(getById(1, lst)) == 1
    assert getNume(getById(1, lst)) == "Nume"
    assert getClasa(getById(1, lst)) == "economy"
    assert getPret(getById(1, lst)) == 1.9
    assert getCheckin(getById(1, lst)) == "Da"

def testModificaRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "economy", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "economy plus", 3.0, "Nu", lst)

    lst = modificaRezervare(1, "newNume", "business", 2.5, "Nu", lst)

    assert len(lst) == 2
    assert getId(getById(1, lst)) == 1
    assert getNume(getById(1, lst)) == "newNume"
    assert getClasa(getById(1, lst)) == "business"
    assert getPret(getById(1, lst)) == 2.5
    assert getCheckin(getById(1, lst)) == "Nu"

def testStergeRezervare():
    lst = []
    lst = adaugaRezervare(1, "Nume", "business", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "business", 3.0, "Nu", lst)

    lst = stergeRezervare(1, lst)
    assert len(lst) == 1

def testGetById():
    lst = []
    lst = adaugaRezervare(1, "Nume", "business", 1.9, "Da", lst)
    lst = adaugaRezervare(2, "Nume2", "business", 3.0, "Nu", lst)

    assert getById(1, lst) == {"id":1, "nume":"Nume", "clasa":"business", "pret":1.9, "checkin":"Da"}