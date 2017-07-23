# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

DEBUGGING = False

import time

# Importing Decimal for monetary floating point

# Making JSON play nice
import json

# Getting logging ability
import logging

# Importing all the custom packages
from packages.header import *
from packages.validation import *
from packages.user import *
from packages.customsql import *
from packages.payment import *

# Getting the pretty colors set up
from packages.colorama import init
init()
from packages.colorama import Fore, Back, Style


def clean_shutdown():
    print(Back.RED + "shutting down..." + Style.RESET_ALL)
    exit()

def show_total(userList):
    SUBTOTAL = 0
    for person in userList:
        print("")
        userList[person].print_receipt()
        SUBTOTAL += userList[person].get_total()
    print("\nSUBTOTAL = " + str(SUBTOTAL))




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
            elif (userInput == jsonObject['KILL_COMMANDS']['ready_for_payment']['name']): break

            # Checking if input is an item in inventory
            elif (userInput in jsonObject['UPC']):
                #check if limit has been reached - this inlcudes cafeteria and packages
                if (userList[current_user].get_quantity(userInput) >= int(jsonObject['UPC'][str(userInput)]['limit'])):
                    print(Fore.YELLOW + "There is a limit of " + str(jsonObject['UPC'][str(userInput)]['limit']) + " for this item" + Style.RESET_ALL)

                #yearbook
                    #quarter ad
                    #half ad
                    # full ad
                    # parking pass
                # lanyard
                # agenda
                # service_club
                    # cafeteria
                    # pac dues

                # uknight patron
                # id badge
                else:
                    userList[current_user].add_item(userInput) # adding item to user's cart
                    #userList[current_user].add_credit(userInput) # adding credit for item to user's cart
                    print(Fore.GREEN + userInput + " added to " + str(userList[current_user].propername) + " cart" + Style.RESET_ALL)

            # Checking if input is a student ID
            elif (lchs_test.is_student(userInput)):
                entry = {userInput: User(userInput, "fname", "lname", "propername", "year", "enrolled", jsonObject)} # creating new user
                userList.update(entry) # adding user to userList
                current_user = userInput # making new user the current user
                print(Fore.MAGENTA + "current user changed to:" + str(userInput) + Style.RESET_ALL)

            else:
                print(Fore.RED + "invalid input" + Style.RESET_ALL)



        SUBTOTAL = 0
        for person in userList:
            print("")
            userList[person].print_receipt()
            SUBTOTAL += userList[person].get_total()
        print("\nSUBTOTAL = " + str(SUBTOTAL))




        #----------------------------------------------
        # Getting payment information
        #----------------------------------------------
        paymentInfo = [] # structure to hold the different payments' info
        outstanding = float(round(SUBTOTAL,2)) # the remaining balance due on the transaction
        print(Fore.YELLOW + "\nWARNING: a 3% fee will be applied to credit card purchases!" + Style.RESET_ALL) # cc surcharge warning
        while (outstanding > round(0.0,2)):
            pay_method = get_payment_method("Method of payment? (" + str(outstanding) + " outstanding): ")

            # Checking for kill command
            if (pay_method == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            amount = get_payment_amount("\tamount: ")

            # Checking for kill command
            if (amount == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            #----------------------------------------------
            # Determining payment method
            #----------------------------------------------
            # Cash
            if (pay_method == jsonObject['VALID_PAYMENT']['cash']['UPC']):
                outstanding = outstanding - float(round(amount,2))
                paymentInfo.append(Payment(pay_method, amount))

            # Check
            elif (pay_method == jsonObject['VALID_PAYMENT']['check']['UPC']):
                outstanding = outstanding - float((round(amount,2)))
                comment = raw_input("\tCheck number: ")
                paymentInfo.append(Payment(pay_method, amount, comment))

            # Card
            elif (pay_method == jsonObject['VALID_PAYMENT']['credit']['UPC']):
                upcharge = float(amount * 0.03)
                print(Fore.YELLOW + "\t3% charge of " + str(upcharge) + " being applied" + Style.RESET_ALL)
                comment = last_four("\tLast four digits on card: ")
                outstanding -= amount
                outstanding += round(upcharge,2)
                paymentInfo.append(Payment(pay_method, amount, comment))

        #print paymentInfo
        print("-"*55)
        print("{0:25} {1:20} {2:7}".format("Type", "Amount", "Comment"))
        print("-"*55)
        for x in paymentInfo:
            x.printInfo()


        ready_to_finish = get_yes_no("Do the above charges look correct?: ")
        if (ready_to_finish == "n"):
            clean_shutdown()
        # Checking for kill command
        if (ready_to_finish == jsonObject['KILL_COMMANDS']['kill_session']['name']):
            clean_shutdown()


        # Printing Receipt
        print(Fore.MAGENTA + "Printing receipt..." + Style.RESET_ALL)


        transaction_end(transaction_number)
        print("\n\n\n\n")

if __name__ == '__main__':
    main()
