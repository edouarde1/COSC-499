import unittest
from selectSort import sortNums




class Test(unittest.TestCase):
    def test_sorted(self):
        self.assertEquals([1,2,3,4,5], sortNums([5,2,3,4,1]))

if __name__ == "__main__":
    unittest.main()