import unittest
from . import tests

class FullTest(unittest.TestCase):
  def setUp(self):
    pass
  
  def test_version(self):
    self.assertTrue(get_version())
    
    
    
if __name__ == '__main__':
  unittest.main()
