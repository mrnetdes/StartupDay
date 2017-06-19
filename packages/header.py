from packages.bcolors import *

def title():
    print("///////////////////////////////////////////////////////////////////////")
    print("////                       STARTUP DAY TOOL                        ////")
    print("////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////")
    print("///////////////////////////////////////////////////////////////////////")

def transaction(number):
    print(bcolors.HEADER + "------------------ Transaction " + number + " ------------------" + bcolors.ENDC)
