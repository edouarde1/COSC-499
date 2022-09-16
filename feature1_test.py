import unittest
from selectSort import sortNums




class Test(unittest.TestCase):
    def test_sorted(self):
        unsortedInput = [5,2,3,4,1]
        
        print('Unsorted Input:', unsortedInput)
        
        sortedOutput = sortNums(unsortedInput)

        print('Sorted Output:', sortedOutput)

        self.assertEquals([1,2,3,4,5],sortedOutput)

if __name__ == "__main__":
    unittest.main()