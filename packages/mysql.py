import mysql.connector

config = {
  'user': 'test',
  'password': 'test',
  'host': 'test',
  'database': 'employees'
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
    
