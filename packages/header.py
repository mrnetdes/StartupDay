#from packages.colorama import Fore, Back, Style
from colorama import Fore, Back, Style

def title():
    print(Back.BLUE + "///////////////////////////////////////////////////////////////////////")
    print("////                       STARTUP DAY TOOL                        ////")
    print("////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////")
    print("///////////////////////////////////////////////////////////////////////" + Style.RESET_ALL)

def transaction(number):
    print(Back.MAGENTA + "\n                      Start Transaction " + str(number) + "                  " + Style.RESET_ALL)

def transaction_end(number):
    print(Back.MAGENTA + "\n                      End Transaction " + str(number) + "                    " + Style.RESET_ALL)
