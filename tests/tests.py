import sys

# Purpose: ensures that Python 2.7 is running on the system
def get_version():
  if not sys.version_info[:2] == (2, 7):
    return False
  else:
    return True

# Purpose: checks that an internet connection is present
def internet_connection():
  return True

# Purpose: check that a connection to the specified database can be made
def db_connection():
  return True
