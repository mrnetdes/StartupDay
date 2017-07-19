# MySQL functionality
import mysql.connector
from mysql.connector import errorcode

import logging


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
        
        config = {
            'user': self.user,
            'password': self.pw,
            'host': self.host,
            'port': self.port,
            'database': self.database
        }
        
    def open_connection(self):
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            logging.info("MySQL: connection to " + str(self.host) + " was successfull")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Uh oh :( Please show this message to your IT Administrator")
                print(str(errorcode.ER_ACCESS_DENIED_ERROR))
                logging.exception("MySQL: Attempting to connect to " + str(self.host) + ":" + str(errorcode.ER_ACCESS_DENIED_ERROR))
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Uh oh :( Please show this message to your IT Administrator")
                print(str(errorcode.ER_ACCESS_DENIED_ERROR))
                logging.exception("MySQL: " + str(errorcode.ER_BAD_DB_ERROR))
            else:
                print("Uh oh :( Please show this message to your IT Administrator")
                print(err)
                logging.exception("MySQL: " + str(err))

                
    def test_connection(self):
        """
        Attempts to connect to the host, ensuring there is a connection
        """
        print ("Testing MySQL connection..."),
        try:
            cnx = mysql.connector.connect(**config)
            print("success!")
            logging.info("MySQL: test connection to ___ was successfull")
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("FAIL! Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("FAIL! Database does not exist")
            else:
                print(err)
                
    
    def close_connection(self):
        cursor.close()
        cnx.close()
        





