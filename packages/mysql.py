# MySQL functionality
import mysql.connector
from mysql.connector import errorcode


class Mysql(object):
    """ Mysql has the following properties:
        user:
        pw:
        host:
        port:
        database:
    """
    def __init__(self, user = "root", pw = "root", host = "localhost", port = 3306, database = ""):
        self.user = user
        self.pw = pw
        self.host = host
        self.port = port
        self.database = database

    def test_connection(self):
        """
        Attempts to connect to the host, ensuring there is a connection
        """
        config = {
            'user': self.user,
            'password': self.pw,
            'host': self.host,
            'port': self.port,
            'database': self.database
        }
        print ("Testing MySQL connection..."),
        try:
            cnx = mysql.connector.connect(**config)
            print("success!")
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("FAIL! Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("FAIL! Database does not exist")
            else:
                print(err)





"""--------------------------------------------------------------------------"""
def main():
    LCHS = Mysql()
    LCHS.test_connection()



main()
