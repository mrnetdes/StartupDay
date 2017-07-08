class User(object):
    """Users have the following properties:
    Attributes:
        userid: a string holding a unique 5 digit number that corresponds to the database
        fname: a string representing the user's first name
        lname: a string representing the user's last name
        propername: a string with the user's propername, which is usually their legal name
        year: an integer representing the user's graduation year

        inventory: a dictionary that holds the item name as a string in the key, and the units of
               item being purchased as an integer in the value
        total: float that will contain the total price of all the items in the User's inventory
    """
    def __init__(self, userid, fname, lname, propername, year):
        # Personal information
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.propername = propername
        self.year = year

        # Inventory information (key=item name, value=units being purchased)
        self.inventory = {'YEARBOOK':0, 'QUARTER_AD':0, 'HALF_ADD':0, 'FULL_AD':0, 'CAFETERIA':0, 'OTHER':0, 'LANYARD':0, 'AGENDA':0, 'PARKING_PASS':0, 'SERVICE_CLUB':0, 'PAC_DUES':0, 'OTHER':0}
        # Total price of all items in User's inventory sans possible credit card surcharge
        self.total = 0


    def get_userid(self):
        return self.userid
    def set_userid(self, id):
        self.userid = id

    # Gets the total of the items in the user's inventory: NOT YET WORKING
    def get_total(self):
        for key in self.inventory:
            print(key ,"corresponds to ", self.inventory[key])

    def print_all(self):
        print("")
        print("userid\t" + str(self.userid))
        print("fname\t" + str(self.fname))
        print("lname\t" + str(self.lname))
        print("proper\t" + str(self.propername))
        print("year\t" + str(self.year))
        for x in self.inventory:
            print(str(x) + '\t' + str(self.inventory[x]))
        print("")
