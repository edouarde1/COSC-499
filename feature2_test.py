import unittest
from selectSort import sortChars




class Test(unittest.TestCase):
    def test_sorted(self):
        self.assertEquals(['a','b','c','d','e'], sortChars(['e','b','a','c','d']))

if __name__ == "__main__":
    unittest.main()