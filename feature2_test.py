import unittest
from selectSort import sortChars




class Test(unittest.TestCase):
    def test_sorted(self):
        unsortedInput = ['e','b','a','c','d']
        
        print('Unsorted Input:', unsortedInput)
        
        sortedOutput = sortChars(unsortedInput)

        print('Sorted Output:', sortedOutput)

        self.assertEquals(['a','b','c','d','e'],sortedOutput)
        

if __name__ == "__main__":
    unittest.main()