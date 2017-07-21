# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

DEBUGGING = True

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

        #----------------------------------------------
        # Variable initialization
        #----------------------------------------------
        """ This isn't required in python, but I think should always be done for proper programming """
        userList = {} # dictionary that contains all the users on a transaction - this is reset for each new transaction
        transaction_number = None # used to hold a unique transaction value
        user_id = None #
        entry = None #
        
        #----------------------------------------------
        # Getting a valid user id
        #----------------------------------------------
        user_id = get_id("Please SCAN Student Number: ")
        # Checking for shutdown command
        if (user_id == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            clean_shutdown()
        fname = "Stephen" #debugging
        lname = "Ritchie" #debugging
        propername = "Stephen Frederick Ritchie" #debugging
        year = "2020" #debugging
        enrolled = "2016" #debugging

        #----------------------------------------------
        # Creating initial user 
        #----------------------------------------------
        entry = {user_id: User(user_id, fname, lname, propername, year, enrolled, jsonObject)} # putting info into a dict to update userList
        userList.update(entry) # updating userList with new user
        current_user = user_id # setting them as the current user

        #----------------------------------------------
        # Generating transaction number
        #----------------------------------------------
        transaction_number = time.time()
        transaction(transaction_number)
        
        print(Fore.MAGENTA + "current user: " + str(userList[current_user].propername) + Style.RESET_ALL)

        #------------------------------------------------------------------
        # Main scanning loop
        #------------------------------------------------------------------
        """ This loop allows the operator to scan items, or scan an id number and create a new user. """
        while True:
            userInput = raw_input("\nPlease SCAN an item or student number: ")
            
            #----------------------------------------------
            # Determining what was entered
            #----------------------------------------------
            # Checking for shutdown command
            if (userInput == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            # Checking for break command
            elif (userInput == jsonObject['KILL_COMMANDS']['read_for_payment']['name']): break

            # Checking if input is an item in inventory 
            elif (userInput in jsonObject['UPC']):
                userList[current_user].add_item(userInput) # adding item to user's cart
                userList[current_user].add_credit(userInput) # adding credit for item to user's cart
                print(Fore.GREEN + userInput + " added to " + str(userList[current_user].propername) + " cart" + Style.RESET_ALL)

            # Checking if input is a student ID
            elif (lchs_test.is_student(userInput)):
                entry = {userInput: User(userInput, "fname", "lname", "propername", "year", "enrolled", jsonObject)} # creating new user
                userList.update(entry) # adding user to userList
                current_user = userInput # making new user the current user
                print(Fore.MAGENTA + "current user changed to:" + str(userInput) + Style.RESET_ALL)

            else:
                print(Fore.RED + "invalid input" + Style.RESET_ALL)

        # DEBUGGING
        if (DEBUGGING):
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
        # include 3% charge for cc

        # Creating Receipt

        # Storing Receipt Locally and in Database

        # Printing Receipt
        print(Fore.MAGENTA + "Printing receipt..." + Style.RESET_ALL)


        print(Fore.MAGENTA + "___________end of transaction__________" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
