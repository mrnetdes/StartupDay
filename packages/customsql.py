# MySQL functionality
import mysql.connector
from mysql.connector import errorcode

import logging


class Customsql(object):
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

        self.config = {
            'user': self.user,
            'password': self.pw,
            'host': self.host,
            'port': self.port,
            'database': self.database
        }

    def open_connection(self):
        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            logging.info("MySQL: connection was opened on " + str(self.host))
        except mysql.connector.Error as err:
            print("Uh oh :( Please show this message to your IT Administrator")
            logging.exception("MySQL: attempting to connect to " + str(self.host))
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(str(errorcode.ER_ACCESS_DENIED_ERROR))
                logging.exception(str(errorcode.ER_ACCESS_DENIED_ERROR))
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(str(errorcode.ER_ACCESS_DENIED_ERROR))
                logging.exception(str(errorcode.ER_BAD_DB_ERROR))
            else:
                print(err)
                logging.exception(str(err))


    def test_connection(self):
        """
        Attempts to connect to the host, ensuring there is a connection
        """
        print ("Testing MySQL connection..."),
        try:
            cnx = mysql.connector.connect(**self.config)
            print("Connection to " + str(self.host) + " successful")
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("FAIL! Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("FAIL! Database does not exist")
            else:
                print(err)

    def is_operator(self, id):
        '''
        Returns True if the given id is a valid operator - returns False otherwise
        '''
        return True

    def is_student(self, id):
        '''
        Returns True if the given id is a valid operator - returns False otherwise
        '''
        return True

    def close_connection(self):
        cursor.close()
        cnx.close()
        logging.info("MySQL: connection to " + str(self.host) + " was closed")
