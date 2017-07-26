#from packages.colorama import Fore, Back, Style
from colorama import Fore, Back, Style

def title():
    print(Back.BLUE + Fore.WHITE + "///////////////////////////////////////////////////////////////////////" + Style.RESET_ALL)
    print(Back.BLUE + Fore.WHITE + "////                       STARTUP DAY TOOL                        ////" + Style.RESET_ALL)
    print(Back.BLUE + Fore.WHITE + "////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////" + Style.RESET_ALL)
    print(Back.BLUE + Fore.WHITE + "///////////////////////////////////////////////////////////////////////" + Style.RESET_ALL)

def transaction(number):
    print(Back.MAGENTA + "\n-------------------Start Transaction " + str(number) + "------------------" + Style.RESET_ALL)

def transaction_end(number):
    print(Back.MAGENTA + "\n-------------------End Transaction " + str(number) + "--------------------" + Style.RESET_ALL)
