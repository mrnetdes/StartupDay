# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

DEBUGGING = False

import time

# Making JSON play nice
import json

# Getting logging ability
import logging

# Importing all the custom packages
from packages.header import *
from packages.validation import *
from packages.user import *
from packages.customsql import *

# Getting the pretty colors set up
from packages.colorama import init
init()
from packages.colorama import Fore, Back, Style

def clean_shutdown():
    print(Back.RED + "shutting down..." + Style.RESET_ALL)
    exit()


# Importing item list
if (DEBUGGING): print(Fore.CYAN + "\n--Memorizing the config file..." + Style.RESET_ALL)
with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
    jsonObject = json.load(data_file) # parsing file
#print json.dumps(jsonObject, indent=4, sort_keys=True)


def main():

    # Setting up log file
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='run.log', level=logging.DEBUG)
    logging.info('========Program Started========')

    # Opening MySQL connection
    lchs_test = Customsql()
    lchs_test.open_connection()

    # DEBUGGING
    if (DEBUGGING):
        print(Fore.YELLOW + "\nWARNING: program is running in debug mode" + Style.RESET_ALL)
        logging.debug('program is running in debugging mode')

    exitFlag = False # boolean to control exiting of main program loop

    title() # Displaying program title

    # Getting a valid operator id
    operator_id = get_operator("Enter operator ID: ")
    if (operator_id == jsonObject['KILL_COMMANDS']['kill_session']['name']):
        clean_shutdown()
    print(Fore.GREEN + "Hello " + str(operator_id) + "!\n" + Style.RESET_ALL)
    logging.info("operator " + str(operator_id) + " signed in")


    #------------------------------------------------------------------
    # Main program loop
    #------------------------------------------------------------------
    while (exitFlag == False):

        # Variable initialization
        userList = {} # dictionary that contains all the users on a transaction - this is reset for each new transaction
#*************************************************************************************************************************
        # Getting a valid user id
        user_id = get_id("Please SCAN Student Number: ")
        if (user_id == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            clean_shutdown()
        fname = "Stephen" #debugging
        lname = "Ritchie" #debugging
        propername = "Stephen Frederick Ritchie" #debugging
        year = "2020" #debugging
        enrolled = "2016" #debugging

        # Creating initial user and setting them as the current user
        entry = {user_id: User(user_id, fname, lname, propername, year, enrolled, jsonObject)}
        userList.update(entry)
        current_user = user_id

        # Generating transaction number
        transaction_number = time.time()
        transaction(transaction_number)
        print(Fore.MAGENTA + "current user: " + str(userList[current_user].propername) + Style.RESET_ALL)

        # Adding items to transaction/adding new user to transaction
        while True:
            userInput = raw_input("\nPlease SCAN an item or student number: ")
            if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            # Checking for quit command
            if (userInput == 'break'): break

            # Checking if input is an item in inventory and adding it
            elif (userInput in jsonObject['UPC']):
                userList[current_user].add_item(userInput)
                userList[current_user].add_credit(userInput)
                print(Fore.GREEN + userInput + " added to " + str(userList[current_user].propername) + " cart" + Style.RESET_ALL)

            # Checking if input is a student ID
            elif (lchs_test.is_student(userInput)):
                entry = {userInput: User(userInput, "fname", "lname", "propername", "year", "enrolled", jsonObject)}
                userList.update(entry)
                current_user = userInput
                print(Fore.MAGENTA + "current user changed to:" + str(userInput) + Style.RESET_ALL)

            else:
                print(Fore.RED + "invalid input" + Style.RESET_ALL)

        # DEBUGGING
        print("")
        for person in userList:
            userList[person].print_receipt()
            print("")

        # Determining payment methods
        print(Fore.YELLOW + "\nWARNING: a 3% fee will be applied to credit card purchases!" + Style.RESET_ALL) # cc surcharge warning

        """split_count = get_split_count("How many ways is this transaction being split?: ")
        if (split_count == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            clean_shutdown()

        # Getting information on each split
        for x in range (1, split_count+1):
              print("\tPayment number " + str(x))
              payment_type = get_payment_type("\tType: ")
              payment_amount = get_payment_amount("\tAmount: ")
              print("")"""

        # Totaling up all items
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Totaling up all items--" + Style.RESET_ALL)
        # include 3% charge for cc

        # Creating Receipt
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Creating receipt--" + Style.RESET_ALL)
        # Create header...
        # Create body...
        # Create footer...


        # Storing Receipt Locally and in Database
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Storing receipt locally and in database--" + Style.RESET_ALL)
        # Storing locally...
        # Storing in database


        # Printing Receipt
        print(Fore.MAGENTA + "Printing receipt..." + Style.RESET_ALL)


        print(Fore.MAGENTA + "___________end of transaction__________" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
