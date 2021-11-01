from Logic.CRUD import adaugaRezervare
from Tests.runAllTests import runTests
from UI.Console import runMenu
from UI.Commands import runCommands
from utils import getRunMethod

def main():
    runTests()
    lst = []
    runMethod = getRunMethod()

    if runMethod == "menu":
        lst = adaugaRezervare(1, "paul", "economy", 44, "da", lst)
        lst = adaugaRezervare(2, "paul", "economy plus", 33, "nu", lst)
        lst = adaugaRezervare(3, "paul", "business", 2, "da", lst)
        lst = adaugaRezervare(4, "mircea", "economy", 44, "da", lst)

        runMenu(lst)
    
    elif runMethod == "commands":
        runCommands(lst) 

if __name__ == "__main__":
    main()