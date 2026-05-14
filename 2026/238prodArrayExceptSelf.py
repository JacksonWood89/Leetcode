import unittest
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Compute prefixes
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Compute suffixes and multiply with prefixes
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_2(self):
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_all_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([0, 0]), [0, 0])

    def test_multiple_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([0, 1, 0, 5]), [0, 0, 0, 0])

    def test_two_elements(self):
        self.assertEqual(self.solution.productExceptSelf([5, 6]), [6, 5])

    def test_negatives(self):
        self.assertEqual(self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6])

if __name__ == '__main__':
    unittest.main()
