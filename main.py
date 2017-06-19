# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0


# Importing modules to allow for JSON manipulation
import json
from pprint import pprint

# Importing all the custom pancakes
from packages import *




DEBUGGING = True



def main():
    exitFlag = False # boolean to control exiting of main program loop

    # Importing item list
    if (DEBUGGING): print("\n--Importing item list--")
    with open('packages/items.json') as data_file:
        items = json.load(data_file)
    #pprint(items) # this doesn't work correctly yet

    header.title() # title graphic
    
    # Getting a valid operator id
    operator_id = validation.get_operator("Enter operator ID: ")

    #------------------------------------------------------------------
    # Main program loop
    #------------------------------------------------------------------
    while (exitFlag == False):
        
        # Getting a valid user id
        if (DEBUGGING): print("\n--Getting a valid user id--")
        userid = validation.get_id("Please SCAN Student Number: ")

        # Creating user
        # ...

        # Adding items to transaction/adding new user to transaction
        header.transaction("TEST") # printing transaction text to screen
        # ...

        # Determining payment methods
        if (DEBUGGING): print("\n--Determining payment methods--")
        print("WARNING: a 3% fee will be applied to credit card purchases!") # cc surcharge warning
        split_count = input("How many ways is this transaction being split?: ") # this needs validation
        for x in range (1, split_count+1):
              print("\tPayment number " + str(x))
              payment_type = validation.get_payment_type("Type: ")
              payment_amount = validation.get_payment_amount("Amount: ")


        # Totaling up all items
        if (DEBUGGING): print("\n--Totaling up all items--")
        # include 3% charge for cc

        # Creating Receipt
        if (DEBUGGING): print("\n--Creating receipt--")


        # Storing Receipt Locally and in Database
        if (DEBUGGING): print("\n--Storing receipt locally and in database--")


        # Printing Receipt
        if (DEBUGGING): print("\n--Printing receipt--")





main()
