# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0


# Making JSON play nice
import json

# Importing all the custom packages
from packages.header import *
from packages.validation import *
from packages.user import *
from packages.mysql import *

# Getting the pretty colors set up
from packages.colorama import init
init()
from packages.colorama import Fore, Back, Style


DEBUGGING = True

# Importing item list
if (DEBUGGING): print(Fore.MAGENTA + "\n--Importing item list--" + Style.RESET_ALL)
with open('config.json', "r") as data_file: # Reading in JSON file to be parsed
    jsonObject = json.load(data_file) # parsing file
if (DEBUGGING):
    pass
    #print json.dumps(jsonObject, indent=4, sort_keys=True)
    #print("A " + str(parsed['items'][0]['name']) + " costs " + str(parsed['items'][0]['price']))


def main():
    exitFlag = False # boolean to control exiting of main program loop




    # Displaying program title
    title()


    # Getting a valid operator id
    if (DEBUGGING): print(Fore.MAGENTA + "\n--Getting a valid operator id--" + Style.RESET_ALL)
    operator_id = get_operator("Enter operator ID: ")
    print(Fore.GREEN + "Hello " + str(operator_id) + "!\n" + Style.RESET_ALL)

    #------------------------------------------------------------------
    # Main program loop
    #------------------------------------------------------------------
    while (exitFlag == False):

        userList = [] # array that contains all the users on a transaction - this is reset for each new transaction

        # Getting a valid user id
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Getting a valid user id--" + Style.RESET_ALL)
        user_id = get_id("Please SCAN Student Number: ")


        # Getting user informatiom
        # ...
        fname = "John"
        lname = "Doe"
        propername = "Johnathan Doe"
        year = "2020"
        enrolled = "2016"


        # Creating user
        userList.append(User(user_id, fname, lname, propername, year, enrolled, jsonObject)) # need to figure out approach to get rest of information
        userList[0].print_all()


        # Adding items to transaction/adding new user to transaction
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Adding items to transaction/adding new user to transaction--" + Style.RESET_ALL)
        #header.transaction("TEST") # printing transaction text to screen
        #userInput =


        #*******************************************************************************

        # Determining payment methods
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Determining payment methods--" + Style.RESET_ALL)
        print(Fore.YELLOW + "WARNING: a 3% fee will be applied to credit card purchases!" + Style.RESET_ALL) # cc surcharge warning
        split_count = get_split_count("How many ways is this transaction being split?: ")

        # Getting information on each split
        for x in range (1, split_count+1):
              print("\tPayment number " + str(x))
              payment_type = get_payment_type("\tType: ")
              payment_amount = get_payment_amount("\tAmount: ")
              print("")


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
        if (DEBUGGING): print(Fore.MAGENTA + "\n--Printing receipt--" + Style.RESET_ALL)
        # NEED ABILITY TO REPRINT RECEIPT





main()
