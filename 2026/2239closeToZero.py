class Solution:
    def findClosestNumber(self, nums) -> int:
        min = nums[0]
        for i in nums:
            if abs(i) < abs(min):
                min = i
            elif abs(i) == abs(min) and i > 0:
                min = i
        
        return min


sol = Solution()

assert sol.findClosestNumber([-4, -2, 1, 4, 8]) == 1
assert sol.findClosestNumber([2, -1, 1]) == 1
assert sol.findClosestNumber([-3, -2, 4, 8]) == -2
assert sol.findClosestNumber([2, 5, 8]) == 2
assert sol.findClosestNumber([-5, -3, -8]) == -3
assert sol.findClosestNumber([100, -100, 0, 5]) == 0
assert sol.findClosestNumber([10]) == 10
assert sol.findClosestNumber([100000, -100000]) == 100000

print("All tests passed!")
