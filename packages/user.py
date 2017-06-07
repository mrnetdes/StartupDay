class User(object):
    """Users have the following properties:
    
    Attributes:
        userid: an integer holding a unique 5 digit number that corresponds to the database
        fname: a string representing the user's first name
        lname: a string representing the user's last name
        propername: a string with the user's propername, which is usually their legal name
        year: an integer representing the user's graduation year
    """
    
    def __init__(self):
        # Personal information
        self.userid = "99999"
        self.fname = "fname"
        self.lname = "lname"
        self.propername = "propername"
        self.year = "2014"
        
        
    def get_userid(self):
        return self.userid
    def set_userid(self, id):
        self.userid = id
        
    
    

