from Tests.testDomain import testDomain
from Tests.testCRUD import *
from Tests.testFunctionalitati import *


def runTests():
    testDomain()
    testCreazaRezervare()
    testModificaRezervare()
    testStergeRezervare()
    testGetById()
    testReducerePretLaCheckinFacut()
    testUpgradeClasaByNume()
    testPretMaxPerClasa()
    testOrdonareDescDupaPret()
    TestTotalPreturiPerNume()
    testUndoRedo()
