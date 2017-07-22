class Payment(object):
    """
    """

    def __init__(self, type, amount, comment="n/a"):
        self.type = type
        self.amount = amount
        self.comment = comment

    def printInfo(self):
        print("{0:25} {1:20} {2:7}".format(str(self.type), str(self.amount), str(self.comment)))
