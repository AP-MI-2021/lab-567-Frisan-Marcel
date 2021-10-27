from Tests.testDomain import testDomain
from Tests.testCRUD import *

def runTests():
    testDomain()
    testCreazaRezervare()
    testModificaRezervare()
    testStergeRezervare()
    testGetById()