class Payment(object):
    """
    Stores information about a payment.
    
    Args:
        type (str): contains the payment method (cash, check, card, etc)
        amount (float): contains the amount in dollars of the payment
        memo (str): field that contains additional info - For example, it will contain the last 4 digits of a cc or the check number of a check
        
    Attributes:
        type (str): contains the payment method (cash, check, card, etc)
        amount (float): contains the amount in dollars of the payment
        memo (str): field that contains additional info - For example, it will contain the last 4 digits of a cc or the check number of a check
    """

    def __init__(self, type, amount, memo=""):
        self.type = type
        self.amount = amount
        self.memo = memo

    def printInfo(self):
        """ Prints out the attributes of the object """
        print("{0:25} {1:20} {2:7}".format(str(self.type), str(self.amount), str(self.memo)))
