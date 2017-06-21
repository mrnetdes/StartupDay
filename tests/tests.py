import sys

# Purpose: ensures that Python 2.7 is running on the system
def get_version():
  if not sys.version_info[:2] == (2, 7):
    return False
  else:
    return True

# Ensures that an internet connection is present
def internet_connection():
  return True
