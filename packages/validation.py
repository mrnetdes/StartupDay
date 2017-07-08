from packages.colorama import Fore, Back, Style

# purpose:
# precondition: string that is prompt user sees
# postcondition:
def get_payment_type(prompt):
    while True:
        # Exception handling for string type
        try:
            userInput = str(input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT " + Style.RESET_ALL + prompt)
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


# purpose: To validate that a given operator id exists...should be done with mysql
# precondition: string that is prompt user sees
# postcondition: returns the operator id once a valid one is given
def get_operator(prompt):
    while True:
        # Exception handling for string
        try:
            userInput = str(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        if (userInput != "SR"):
            print(Fore.RED + "Invalid Operator!" + Style.RESET_ALL)
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
            userInput = int(raw_input(prompt))
        except ValueError:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            continue

        # Custom validation for proper ID number
        if (userInput != 9):
            print(Fore.RED + "STUDENT NUMBER NOT FOUND " + Style.RESET_ALL)
            continue
        else:
            break

    return userInput
