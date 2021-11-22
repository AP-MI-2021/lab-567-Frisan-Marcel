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
        runMenu(lst)
    elif runMethod == "commands":
        runCommands(lst) 

if __name__ == "__main__":
    main()