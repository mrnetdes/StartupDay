#from packages.colorama import Fore, Back, Style
from colorama import Fore, Back, Style

def title():
    print(Back.BLUE + "///////////////////////////////////////////////////////////////////////")
    print("////                       STARTUP DAY TOOL                        ////")
    print("////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////")
    print("///////////////////////////////////////////////////////////////////////" + Style.RESET_ALL)

def transaction(number):
    print(Fore.MAGENTA + "\n__________________________ Transaction " + str(number) + " ___________________________" + Style.RESET_ALL)
