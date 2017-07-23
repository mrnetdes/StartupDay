# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

DEBUGGING = False



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


import json
import logging
import time

logging.basicConfig(filename='run.log',format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logging.info("-----Program Started-----")


def clean_shutdown():
    lchs_test.close_connection()
    logging.info("shutdown command was issued")
    print(Back.RED + "shutting down..." + Style.RESET_ALL)
    exit()

def show_total(userList):
    SUBTOTAL = 0
    for person in userList:
        print("")
        userList[person].print_receipt()
        SUBTOTAL += userList[person].get_total()
    print("\nSUBTOTAL = " + str(SUBTOTAL))

def main():

    # Variables initialization
    jsonObject = None
    lchs_test = None
    exitFlag = None
    operator_id = None
    transaction_number = None
    user_id = None
    entry = None
    userList = None
    current_user = None


    # Importing item list
    with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
        jsonObject = json.load(data_file) # parsing file
    #print json.dumps(jsonObject, indent=4, sort_keys=True)



    # Opening MySQL connection
    lchs_test = Customsql()

    # DEBUGGING
    if (DEBUGGING):
        print(Fore.YELLOW + "WARNING: program is running in debug mode" + Style.RESET_ALL)
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
        transaction_number = None # used to hold a unique transaction value
        user_id = None #
        entry = None #
        userList = {}

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
        current_user = int(user_id) # making new user the current user
        entry = {current_user: User(current_user, fname, lname, propername, year, enrolled, jsonObject)} # creating new user
        userList.update(entry) # adding user to userList


        #----------------------------------------------
        # Generating transaction number
        #----------------------------------------------
        transaction_number = 1234
        transaction(transaction_number)

        print(Fore.MAGENTA + "current user: " + str(userList[current_user].userid) + Style.RESET_ALL)


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

                # Checking if user already exists in transaction
                if userList.has_key(int(userInput)):
                    print(Fore.MAGENTA + "user already exists" + Style.RESET_ALL)
                    current_user = int(userInput)
                    print(Fore.MAGENTA + "current user changed to:" + str(userList[current_user].userid) + Style.RESET_ALL)

                # Adding new user since they don't already exist
                else:
                    current_user = int(userInput) # making new user the current user
                    entry = {current_user: User(current_user, "fname", "lname", "propername", "year", "enrolled", jsonObject)} # creating new user
                    userList.update(entry) # adding user to userList
                    print(Fore.MAGENTA + "current user changed to:" + str(userList[current_user].userid) + Style.RESET_ALL)

            else:
                print(Fore.RED + "invalid input" + Style.RESET_ALL)


        if (DEBUGGING):
            for person in userList:
                print(Fore.CYAN),
                print(person, userList[person]),
                print(Style.RESET_ALL)

        print(Fore.MAGENTA + "--------------------------------------------------------------" + Style.RESET_ALL)

        SUBTOTAL = 0
        for person in userList:
            print("")
            userList[person].print_receipt()
            SUBTOTAL += userList[person].get_total()
        print("\nTOTAL = " + str(SUBTOTAL))


        #----------------------------------------------
        # Getting payment information
        #----------------------------------------------
        paymentInfo = [] # structure to hold the different payments' info
        outstanding = float(round(SUBTOTAL,2)) # the remaining balance due on the transaction
        print(Fore.YELLOW + "\nWARNING: a 3% fee will be applied to credit card purchases!" + Style.RESET_ALL) # cc surcharge warning
        print(Fore.YELLOW + "True total may be up to $" + str(float(SUBTOTAL) * 1.03)+ Style.RESET_ALL)
        while (outstanding > round(0.0,2)):
            pay_method = get_payment_method("Method of payment? ($" + str(outstanding) + " outstanding): ")

            # Checking for kill command
            if (pay_method == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            amount = get_payment_amount("\tamount: ")

            # Checking for kill command
            if (amount == jsonObject['KILL_COMMANDS']['kill_session']['name']):
                clean_shutdown()

            # Checking for pay in full


            #----------------------------------------------
            # Determining payment method
            #----------------------------------------------
            # Cash
            if (pay_method == jsonObject['VALID_PAYMENT']['cash']['UPC']):
                if (str(amount) == jsonObject['VALID_PAYMENT']['pay_in_full']['UPC']):
                    amount = float(outstanding)
                    outstanding = 0
                    paymentInfo.append(Payment(pay_method, amount))
                else:
                    outstanding = float(outstanding) - float(round(amount,2))
                    paymentInfo.append(Payment(pay_method, amount))

            # Check
            elif (pay_method == jsonObject['VALID_PAYMENT']['check']['UPC']):
                comment = raw_input("\tCheck number: ")
                if (amount == jsonObject['VALID_PAYMENT']['pay_in_full']['UPC']):
                    amount = float(outstanding)
                    outstanding = 0
                    paymentInfo.append(Payment(pay_method, amount))
                else:
                    outstanding = outstanding - float((round(amount,2)))
                    paymentInfo.append(Payment(pay_method, amount, comment))

            # Card
            elif (pay_method == jsonObject['VALID_PAYMENT']['credit']['UPC']):
                comment = last_four("\tLast four digits on card: ")
                if (amount == jsonObject['VALID_PAYMENT']['pay_in_full']['UPC']):
                    upcharge = float(outstanding * 0.03)
                    amount = float(outstanding + upcharge)
                    outstanding = 0
                    print(Fore.YELLOW + "\t3% charge of $" + str(upcharge) + " being applied" + Style.RESET_ALL)
                    paymentInfo.append(Payment(pay_method, amount, comment))
                else:
                    upcharge = float(amount * 0.03)
                    print(Fore.YELLOW + "\t3% charge of $" + str(upcharge) + " being applied" + Style.RESET_ALL)
                    outstanding -= amount
                    outstanding += round(upcharge,2)
                    paymentInfo.append(Payment(pay_method, amount, comment))

        #print paymentInfo
        print("-"*55)
        print("{0:25} {1:20} {2:7}".format("Payment", "Amount", "Comment"))
        print("-"*55)
        for x in paymentInfo:
            x.printInfo()


        ready_to_finish = get_yes_no("\nDo the above charges look correct?: ")
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
