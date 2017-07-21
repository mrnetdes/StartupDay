class User(object):
    """Users have the following properties:
    Attributes:
        userid: unique id number of a user
        fname: first name
        lname: last name
        propername: full propername, since sometimes fname is a nickname
        year: the year that the user will r
        enrollment_year:

        jsonObject:
        cart:
        total:
    """

    def __init__(self, userid, fname, lname, propername, year, enrollment_year, jsonObject):
        # Personal information
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.propername = propername
        self.year = year # year user will graduate LCHS
        self.enrollment_year = enrollment_year # the school year user started at LCHS

        # Inventory and cart information
        self.jsonObject = jsonObject # item information as json object
        self.cart = {} # user's cart to hold item/amount information
        self.credits = {} #user's cart to hold item/amount of item credits

        # Adding items to cart and credits- initializing with 0 units of each item
        for item in self.jsonObject['UPC']:
            self.cart[str(item)] = 0
            self.credits[str(item)] = 0

    def get_total(self):
        """ Gets the total of the items in the user's cart minus their credits """
        total = 0.0
        for item in self.cart:
            total += float(self.cart[item] * self.jsonObject['UPC'][item]['price'])
        for item in self.credits:
            total += float(self.credits[item] * self.jsonObject['UPC'][item]['credit_price'])
        return total

    def add_item(self, UPC):
        """ Increments the quantity of the given UPC in the cart. """
        self.cart[str(UPC)] += 1

    def add_credit(self, UPC):
        """ Increments the quantity of the given UPC in the credits cart """
        self.credits[str(UPC)] += 1

    def print_receipt(self):
        print('Name: ' + str(self.propername))
        print("ID: " + str(self.userid))
        print('Grade: ' + str(self.year))
        print('Enrollment: ' + str(self.enrollment_year))
        print("Total\t" + str(self.get_total()))
        print "-"*60
        print(" {: <20}{: <25}{: <18}".format("Item", "Amount", "Cost"))
        print "-"*60
        for x in self.cart:
            name = str(self.jsonObject['UPC'][x]['name'])
            price = str(self.cart[x] * self.jsonObject['UPC'][x]['price'])
            quantity = str(self.cart[x])
            print(" {: <20}{: <25}{: <18}".format(name, quantity, price))
        for x in self.credits:
            name = str("cred: ") + str(self.jsonObject['UPC'][x]['name'])
            price = str(self.cart[x] * self.jsonObject['UPC'][x]['credit_price'])
            quantity = str(self.cart[x])
            print(" {: <20}{: <25}{: <18}".format(name, quantity, price))
