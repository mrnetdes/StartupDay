import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': ''
}

def mysql_test_connection():
  try:
    cnx = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your username or password")
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()


"""--------------------------------------------------------------------------"""
def main():
    mysql_test_connection()
main()
