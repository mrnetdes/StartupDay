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
        print("Invalid operator...")
        userInput = input("Please enter your operator id:)
    operator_id = userInput
        
    
    # Main program loop
    while (!exitFlag):
 
        # Getting a valid user id
        userInput = input("Please scan an ID number")
        while(!check_id(userInput):
              print("Invalid ID...")
              userInput = input("Please scan an ID number:")
              
              
    
    
    
#--------------------------------------------------------------------------------------    
def cleanShutdown():
    exit("Performing a clean shutdown...")
  
# check for exit command              
def check_id(id):
    return True

# check for exit command
def check_operator(id):
    return True
    


main()
