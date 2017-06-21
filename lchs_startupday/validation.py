class Validation:
    # purpose:
    # precondition: string that is prompt user sees
    # postcondition:
    def get_payment_type(prompt):
        while True:
            # Exception handling for string type
            try:
                userInput = str(input(prompt))
            except ValueError:
                print(bcolors.FAIL + "INVALID INPUT " + bcolors.ENDC + prompt)
                continue

            # Custom validation for cash, check, or credit card
            if (userInput != "cash" or userInput != "check" or userInput != "creditcard"):
                print(bcolors.FAIL + "INVALID INPUT " + bcolors.ENDC + prompt)
                continue
            else:
                break

        return userInput


    # purpose:
    # precondition: string that is prompt user sees
    # postcondition:
    def get_payment_amount(prompt):
        while True:
            # Exception handling for float
            try:
                userInput = float(input(prompt))
            except ValueError:
                print(bcolors.FAIL + "INVALID PAYMENT TYPE " + bcolors.ENDC + prompt)
                continue

            # Custom validation minimum amount...NEED TO SEE WHAT MIN AND MAX SHOULD BE
            if (userInput < 0):
                print(bcolors.FAIL + "INVALID AMOUNT " + bcolors.ENDC + prompt)
                continue
            else:
                break

        return userInput


    # purpose:
    # precondition:
    # postcondition:
    def get_operator(prompt):
        while True:
            # Exception handling for string
            try:
                userInput = str(input(prompt))
            except ValueError:
                print(bcolors.FAIL + "INVALID INPUT " + bcolors.ENDC+ prompt)
                continue

            # Custom validation for proper operator ID
            if (userInput != "SR"):
                print(bcolors.FAIL + "OPERATOR ID NOT FOUND " + bcolors.ENDC + prompt)
                continue
            else:
                break

        return userInput


    # purpose:
    # precondition:
    # postcondition:
    def get_id(prompt):
        while True:
            # Exception handling for string
            try:
                userInput = int(input(prompt))
            except ValueError:
                print(bcolors.FAIL + "INVALID INPUT " + bcolors.ENDC + prompt)
                continue

            # Custom validation for proper ID number
            if (userInput != 9):
                print(bcolors.FAIL + "STUDENT NUMBER NOT FOUND " + bcolors.ENDC + prompt)
                continue
            else:
                break

        return userInput