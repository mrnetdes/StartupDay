# MySQL functionality
import mysql.connector
from mysql.connector import errorcode
import sys
import json
import logging

user = "root"
pw = "root"
host = "localhost"
port = 3306
database = "lchsdb_test"

config = {
    'user': user,
    'password': pw,
    'host': host,
    'port': port,
    'database': database
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    #logging.info("MySQL: connection was opened on " + str(self.host))
except mysql.connector.Error as err:
    print("Uh oh :( Please show this message to your IT Administrator")
    print(str(err))
    #logging.exception("MySQL: attempting to connect to " + str(self.host))
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #print(str(errorcode.ER_ACCESS_DENIED_ERROR))
        #logging.exception(str(errorcode.ER_ACCESS_DENIED_ERROR))
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #print(str(errorcode.ER_ACCESS_DENIED_ERROR))
        #logging.exception(str(errorcode.ER_BAD_DB_ERROR))
        sys.exit()
    else:
        #print(err)
        #logging.exception(str(err))
        sys.exit()

def is_student(id):
    '''
    Returns True if the given id is a valid operator - returns False otherwise
    '''
    query = "SELECT Fname, Lname, Pname, GradClass, EnrollYear FROM PEOPLE WHERE IDNum=" + str(id) + " AND Status=\"Active\""
    #query = "SELECT COUNT(*) FROM People WHERE IDNum=" + str(id) + " AND Status=\"Active\""
    cursor.execute(query)
    #rows = cursor.fetchone()[0]
    rows = cursor.rowcount
    #print(cursor.rowcount)
    if rows == 0:
        return False
    else:
        return True

    cursor.close()
