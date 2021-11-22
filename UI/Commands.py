from Logic.CRUD import *
from utils import showAll
from Exceptions.CustomExceptions import LogicError

def getCommands(string, lst):
    """
    """
    cmds = string.split(";")
    for cmd in cmds:
        function = cmd.split(",")
        if function[0].lower() == "adauga":
            try:
                lst = adaugaRezervare(function[1], function[2], function[3], function[4], function[5], lst)
                showAll(lst)
            except LogicError as le:
                print(f"Eroare: {le}")
        elif function[0].lower() == "sterge":
            try:
                lst = stergeRezervare(function[1], lst)
                showAll(lst)
            except LogicError as le:
                print(f"Eroare: {le}")
        elif function[0].lower() == "modifica":
            try:
                lst = modificaRezervare(function[1], function[2], function[3], function[4], function[5], lst)
                showAll(lst)
            except LogicError as le:
                print(f"Eroare: {le}")
        elif function[0].lower() == "help":
            print("Programul are implementate urmatoarele functionalitati: ")
            print("adauga (ex: adauga,1,paul,economy,44.5,da)")
            print("sterge (ex: sterge,1)")
            print("modifica (ex: modifica,1,mricea,economy plus,66.6,nu)")
    return lst

def runCommands(lst):
    run = True
    while run:
        cmd = input("Commanda: ")
        lst = getCommands(cmd, lst)