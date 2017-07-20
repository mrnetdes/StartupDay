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

# Support for json config file
import json

# Mysql Support
from packages.customsql import *

import logging

# Importing config file
with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
    jsonObject = json.load(data_file) # parsing file


lchs_test = Customsql()
lchs_test.open_connection()


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
            logging.exception("Invalid input was used for payment type: " + str(userInput))
            continue

        # Custom validation
        if userInput in jsonObject['VALID_PAYMENT']:
            break
        else:
            print(Fore.RED + "\tINVALID PAYMENT TYPE " + Style.RESET_ALL)
            logging.error("Invalid payment type was entered: " + str(userInput))
            continue

        '''
        # Custom validation for cash, check, or credit card
        if ((userInput != str(jsonObject['payment'][0]['type'])) and (userInput != str(jsonObject['payment'][1]['type'])) and (userInput != str(jsonObject['payment'][2]['type']))):
            print(Fore.RED + "\tINVALID PAYMENT TYPE " + Style.RESET_ALL)
            logging.error("Invalid payment type was entered: " + str(userInput))
            continue
        else:
            if (userInput == "check"):
                check_number = int(raw_input("\tPlease enter check number: "))
            break
        '''

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


def get_operator(prompt):
    '''
    '''
    while True:
        # Exception handling for string
        try:
            userInput = str(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            continue
        # Checking that operator is in database
        if (lchs_test.is_operator(userInput)):
            break
        else:
            print(Fore.RED + "Invalid Operator" + Style.RESET_ALL)
            continue
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

        # Custom validation for proper ID number - NOT DONE YE
        if (lchs_test.is_student(userInput)):
            break
        else:
            print(Fore.RED + "STUDENT NUMBER NOT FOUND " + Style.RESET_ALL)
            continue


    return userInput


def get_split_count(prompt):
    """
    purpose: to get a valid integer in the range 1-10 which is used as the
             amount of ways a transaction can be split
    precondtion: prompt that user will see
    postcondition: returns integer from 1-10
    """
    while True:
        # Exception handling for int type
        try:
            userInput = int(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        # Custom validation for integer from 1-10
        if (userInput <= 0 or userInput > 10):
            print(Fore.RED + "SPLIT MUST BE AT LEAST ONE " + Style.RESET_ALL)
            continue
        else:
            break

    return userInput


def get_item(prompt):
    """
    """
    while True:
        # Exception handling for data type
        try:
            userInput = str(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        # Custom validation for item names
        if userInput in jsonObject['UPC']:
            break
        else:
            if (userInput == 'break'):
                break
            # Trying to cast as int to see if input is a student number
            try:
                userInput = int(userInput)
                userInput = get_id("Please SCAN Student Number: ")
                break
            except:
                print(Fore.RED + "Could not find item\t" + str(userInput) + Style.RESET_ALL)
                continue

    return userInput
