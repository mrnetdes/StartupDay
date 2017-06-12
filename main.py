# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

import json
from pprint import pprint






def main():
    exitFlag = False # boolean to control main exiting of main program loop
    
    # Importing item list
    with open('/packages/items.json') as data_file:
        items = json.load(data_file)
    pprint(items)
     
        
    #header.title()
    
    
    # Getting a valid operator id
    userInput = input("Please enter your operator id:")
    while (!check_operator(userInput)):
        userInput = input("INVALID ID: Please enter your operator id:)
    operator_id = userInput
        
    
    # Main program loop
    while (!exitFlag):
 
        # Getting a valid user id
        userInput = input("Please scan an ID number")
        while(!check_id(userInput):
              userInput = input("INVALID ID: Please scan an ID number:")
              
        # Creating user
              
        # Adding items to transaction/adding new user to transaction
              
        # Determining payment methods
        split_count = input("How many ways is this transaction being split?") # this needs validation
        for x in range (1, split_count+1):
              print("Payment number ", x
              payment_type = get_payment_type()
              payment_amount = get_payment_amount()
              
              
        # Creating Receipt
              
              
        # Storing Receipt Locally and in Database
              
              
        # Printing Receipt
              
              
    
    
    
#--------------------------------------------------------------------------------------    
def cleanShutdown():
    
  
# check for exit command              
def check_for_exit(id):
    if (id == "exit"):
        exit("Performing a clean shutdown...")
    return

# check for exit command
def check_operator(id):
    return True

# These functions need validation
def get_payment_type():
    userInput = input("Type:")
    return userInput
def get_payment_amount():
    userInput = input("Amount:")
    return userInput
    


main()
