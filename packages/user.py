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

        # Adding items to cart and credits - initializing with 0 units for each item
        for item in self.jsonObject['UPC']:
            self.cart[str(item)] = 0
            self.credits[str(item)] = 0

    def get_total(self):
        """ Gets the total of the items in the user's cart and their credits """
        total = 0.00 # resetting total to 0
        # Adding all items in cart
        for item in self.cart:
            total += float(self.cart[item] * self.jsonObject['UPC'][item]['price'])
        # Adding all items in credit
        for item in self.credits:
            total += float(self.credits[item] * self.jsonObject['UPC'][item]['credit_price'])
        return float(total)

    def add_item(self, UPC):
        """ Increments the quantity of the given UPC in the cart. """
        self.cart[str(UPC)] += 1

    def add_credit(self, UPC):
        """ Increments the quantity of the given UPC in the credits cart """
        self.credits[str(UPC)] += 1

    def get_quantity(self, UPC):
        """ """
        return int(self.cart[str(UPC)])

    def add_to_cafe(self, amount, UPC):
        """ """
        if ((self.cart[str(UPC)] += float(amount)) < 0):
            print("Amount would make account balance negative and is being ignored"
        else:
            self.cart[str(UPC)] += float(amount)

    def print_info(self):
        """ """
        print("ID: " + str(self.userid))
        print("Name: " + str(self.propername))
        print("Year: " + str(self.year))
        print("Entrolled: " + str(self.enrollment_year))
        print "-"*50
        print("{0:25} {1:20} {2:7}".format("Item", "Amount", "Cost"))
        print "-"*50
        for x in self.cart:
            name = str(self.jsonObject['UPC'][x]['name'])
            price = str(self.cart[x] * self.jsonObject['UPC'][x]['price'])
            quantity = str(self.cart[x])
            print("{0:25} {1:20} {2:7}".format(name, quantity, price))
        for x in self.credits:
            name = str("cred: ") + str(self.jsonObject['UPC'][x]['name'])
            price = str(self.cart[x] * self.jsonObject['UPC'][x]['credit_price'])
            quantity = str(self.credits[x])
            print("{0:25} {1:20} {2:7}".format(name, quantity, price))

    def print_receipt(self):
        """ """
        print("ID: " + str(self.userid)),
        print("Name: " + str(self.propername))
        print("Year: " + str(self.year))
        print "-"*50
        print("{0:20} {1:20} {2:10}".format("Item", "Amount", "Cost"))
        print "-"*50
        for x in self.cart:
            if (self.cart[x] > 0):
                name = str(self.jsonObject['UPC'][x]['name'])
                price = str(self.cart[x] * self.jsonObject['UPC'][x]['price'])
                quantity = str(self.cart[x])
                print("{0:20} {1:20} {2:10}".format(name, quantity, price))
        for x in self.credits:
            if (self.credits[x] > 0):
                name = str("cred: ") + str(self.jsonObject['UPC'][x]['name'])
                price = str(self.cart[x] * self.jsonObject['UPC'][x]['credit_price'])
                quantity = str(self.credits[x])
                print("{0:20} {1:20} {2:10}".format(name, quantity, price))
        print("SUBTOTAL = " + str(self.get_total()))
