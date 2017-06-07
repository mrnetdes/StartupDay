# Author: Stephen Ritchie
# Date: 06/07/2017
# Version: Pre-Alpha 1.0

import json
from pprint import pprint






def main():
    exitFlag = False
    
    # Importing item list
    with open('/packages/items.json') as data_file:
        items = json.load(data_file)
        
    pprint(items)
    
    # Main program loop
    while (!exitFlag):
        userInput = input("Please scan an ID number")
    
    
    
    
def cleanShutdown():
    print("Performing a clean shutdown...")
    


main()
