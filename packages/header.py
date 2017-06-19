import bcolors

title():
    print(bcolors.HEADER + "///////////////////////////////////////////////////////////////////////")
    print("////                       STARTUP DAY TOOL                        ////")
    print("////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2017       ////")
    print("///////////////////////////////////////////////////////////////////////" + bcolors.ENDC)
    
transaction(number):
    print(bcolors.HEADER + "------------------ Transaction " + number + " ------------------" + bcolors.ENDC)
