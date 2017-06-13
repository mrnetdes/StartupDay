import bcolors

title():
    print(bcolors.HEADER + "///////////////////////////////////////////////")
    print("//   LEXINGTON CATHOLIC HIGH SCHOOL         //")
    print("///////////////////////////////////////////////" + bcolors.ENDC)
    
transaction(number):
    print(bcolors.HEADER + "------------------ Transaction " + number + " ------------------" + bcolors.ENDC)
