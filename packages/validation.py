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


# Importing config file
with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
    jsonObject = json.load(data_file) # parsing file

# Connecting to Mysql database
if (jsonObject['ENVIRONMENT'] == "local"):
    print(Fore.CYAN + 'env is local' + Style.RESET_ALL)
    lchs_test = Customsql()
else:
    user = "startup"
    pw = "Lch$Startup"
    host = "lchsweb.lexingtoncatholic.local"
    database = "lchsdb_test"
    lchs_test = Customsql(user, pw, host, database)





def get_payment_amount(prompt):
    """
    """
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            return

        if (userInput == jsonObject['VALID_PAYMENT']['pay_in_full']['UPC']):
            return str(userInput)

        # Exception handling for float
        try:
            userInput = float(userInput)
        except ValueError:
            print(Fore.RED + "\tINVALID INPUT" + Style.RESET_ALL)
            continue

        # Custom validation minimum amount...NEED TO SEE WHAT MIN AND MAX SHOULD BE
        if (userInput < 0):
            print(Fore.RED + "\tINVALID AMOUNT " + Style.RESET_ALL)
            continue
        else:
            break

    return float(round(userInput,2))


def get_operator(prompt):
    '''
    Ready for final review
    '''
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Exception handling for string
        try:
            userInput = str(userInput)
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


def get_id(prompt):
    '''
    Ready for final review
    '''
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Exception handling for string
        try:
            userInput = int(userInput)
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

"""
def get_split_count(prompt):

    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Exception handling for int type
        try:
            userInput = int(userInput)
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
"""

def get_item(prompt):
    """
    """
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Exception handling for data type
        try:
            userInput = str(userInput)
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


def get_payment_method(prompt):
    """
    """
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Custom validation for item names
        if userInput in jsonObject['VALID_PAYMENT']:
            break
        else:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

    return userInput


def get_yes_no(prompt):
    """
    """
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        if (userInput == "y" or userInput == "n"):
            break
        else:
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            continue

    return str(userInput)

def last_four(prompt):
    """
    """
    while True:
        userInput = raw_input(prompt)

        # Checking for kill command
        if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            break

        # Exception handling for data type
        try:
            userInput = int(userInput)
        except ValueError:
            print(Fore.RED + "\tINVALID INPUT" + Style.RESET_ALL)
            continue

        if (len(str(userInput)) == 4):
            break
        else:
            print(Fore.RED + "\tINVALID INPUT" + Style.RESET_ALL)
            continue

    return int(userInput)
