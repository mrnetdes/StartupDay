"""
get_payment_type():
NOT DONE

get_payment_amount():
NOT DONE

get_operator():
NOT DONE

get_id():
NOT DONE

other:

"""


# Getting pretty colors
from packages.colorama import Fore, Back, Style
import json

# Importing config file
with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
    jsonObject = json.load(data_file) # parsing file

def get_payment_type(prompt):
    """
    purpose:
    precondition: prompt that the user sees
    postcondition: string of the payment type selected
    """
    while True:
        # Exception handling for string type
        try:
            userInput = str(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "\tINVALID INPUT " + Style.RESET_ALL)
            continue

        # Custom validation for cash, check, or credit card
        if ((userInput != str(jsonObject['payment'][0]['type'])) and (userInput != str(jsonObject['payment'][1]['type'])) and (userInput != str(jsonObject['payment'][2]['type']))):
            print(Fore.RED + "\tINVALID PAYMENT TYPE " + Style.RESET_ALL)
            continue
        else:
            if (userInput == "check"):
                check_number = int(raw_input("\tPlease enter check number: "))
            break

    return str(userInput)


# purpose:
# precondition: string that is prompt user sees
# postcondition:
def get_payment_amount(prompt):
    while True:
        # Exception handling for float
        try:
            userInput = float(input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID PAYMENT TYPE " + Style.RESET_ALL)
            continue

        # Custom validation minimum amount...NEED TO SEE WHAT MIN AND MAX SHOULD BE
        if (userInput < 0):
            print(Fore.RED + "INVALID AMOUNT " + Style.RESET_ALL)
            continue
        else:
            break

    return userInput


# purpose: To validate that a given operator id exists...should be done with mysql
# precondition: string that is prompt user sees
# postcondition: returns the operator id once a valid one is given
def get_operator(prompt):
    while True:
        # Exception handling for string
        try:
            userInput = str(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        if (userInput != "SR"):
            print(Fore.RED + "Invalid Operator!" + Style.RESET_ALL)
            continue
        else:
            break

    return userInput


# purpose:
# precondition:
# postcondition:
def get_id(prompt):
    while True:
        # Exception handling for string
        try:
            userInput = int(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        # Custom validation for proper ID number - NOT DONE YET
        if (userInput != 9):
            print(Fore.RED + "STUDENT NUMBER NOT FOUND " + Style.RESET_ALL)
            continue
        else:
            break

    return userInput
