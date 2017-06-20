from packages.colorama import Fore, Back, Style

def title():
    print(Fore.CYAN + "///////////////////////////////////////////////////////////////////////")
    print("////                       STARTUP DAY TOOL                        ////")
    print("////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////")
    print("///////////////////////////////////////////////////////////////////////" + Style.RESET_ALL)

def transaction(number):
    print(bcolors.HEADER + "------------------ Transaction " + number + " ------------------" + bcolors.ENDC)
