from Domain.Rezervare import *

def testDomain():
    rezervare = creareRezervare(1, "Hotel", "premium", 44, "da")

    assert getId(rezervare) == 1
    assert getPret(rezervare) == 44
    assert getNume(rezervare) == "Hotel"
    assert getCheckin(rezervare) == "da"
    assert getClasa(rezervare) == "premium"
