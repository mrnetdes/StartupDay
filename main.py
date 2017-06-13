# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0



import json
from pprint import pprint

from packages import *




DEBUGGING = True



def main():
    exitFlag = False # boolean to control main exiting of main program loop

    # Importing item list
    with open('packages/items.json') as data_file:
        items = json.load(data_file)
    #pprint(items) # this doesn't work correctly yet

    header.title() # title graphic


    # Getting a valid operator id
    operator_id = validation.get_operator("Enter operator ID:")


    # Main program loop
    while (exitFlag == False):

        # Getting a valid user id
        if (DEBUGGING): print(bcolors.HEADER + "\n--Getting a valid user id--" + bcolors.ENDC)
        userInput = get_id("Please enter id: ")

        # Creating user

        # Adding items to transaction/adding new user to transaction
        header.transaction("TEST") # printing transaction text to screen

        # Determining payment methods
        if (DEBUGGING): print(bcolors.HEADER + "\n--Determining payment methods--" + bcolors.ENDC)
        print(bcolors.WARNING + "WARNING: a 3% fee will be applied to credit card purchases!" + bcolors.ENDC) # cc surcharge warning
        split_count = input("How many ways is this transaction being split?: ") # this needs validation
        for x in range (1, split_count+1):
              print("\tPayment number " + str(x))
              payment_type = validation.get_payment_type("Type: ")
              payment_amount = validation.get_payment_amount("Amount: ")


        # Totaling up all items
        if (DEBUGGING): print(bcolors.HEADER + "\n--Totaling up all items--" + bcolors.ENDC)
        # include 3% charge for cc

        # Creating Receipt
        if (DEBUGGING): print(bcolors.HEADER + "\n--Creating receipt--" + bcolors.ENDC)


        # Storing Receipt Locally and in Database
        if (DEBUGGING): print(bcolors.HEADER + "\n--Storing receipt locally and in database--" + bcolors.ENDC)


        # Printing Receipt
        if (DEBUGGING): print(bcolors.HEADER + "\n--Printing receipt--" + bcolors.ENDC)





#--------------------------------------------------------------------------------------
#def cleanShutdown():

# purpose:
# precondition:
# postcondition:
def get_id(prompt):
    userInput = input(prompt)
    while True:
        if (userInput != 999):
            userInput = input(bcolors.FAIL + "INVALID ID: " + prompt + bcolors.ENDC)
        else:
            break
    return userInput



# check for exit command
def check_for_exit(id):
    if (id == "exit"):
        exit("Performing a clean shutdown...")
    return

# check for exit command
def check_operator(id):
    return True

# purpose:
# precondition: string that is prompt user sees
# postcondition:
def get_payment_type(prompt):
    while True:
        # Exception handling for string type
        try:
            userInput = str(input(prompt))
        except ValueError:
            print(bcolors.FAIL + "INVALID INPUT " + prompt + bcolors.ENDC)
            continue
        # Custom validation for cash, check, or credit card   
        if (userInput != "cash" or userInput != "check" or userInput != "creditcard"):
            print(bcolors.FAIL + "INVALID INPUT " + prompt + bcolors.ENDC)
            continue
        else:
            break
            
    return userInput
            
# purpose:
# precondition:
# postcondition:
def get_payment_amount(prompt):
    




main()
