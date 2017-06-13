class validation:
    # purpose:
    # precondition: string that is prompt user sees
    # postcondition:
    def get_payment_type(prompt):
        while True:
            # Exception handling for string type
            try:
                userInput = str(input(prompt))
            except ValueError:
                print(bcolors.FAIL + "INVALID INPUT " + prompt + bcolors.ENDC)
                continue
                
            # Custom validation for cash, check, or credit card   
            if (userInput != "cash" or userInput != "check" or userInput != "creditcard"):
                print(bcolors.FAIL + "INVALID INPUT " + prompt + bcolors.ENDC)
                continue
            else:
                break
            
        return userInput
      
    def get_payment_amount(prompt):
  
