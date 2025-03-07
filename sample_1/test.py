import unittest
from sample_1 import testing
from sample_1.testing import sub


class Tests(unittest.TestCase):

      def subtraction(self):
          self.assertEqual(sub(50,20),30)





if __name__ == '__main__':
    unittest.main()
