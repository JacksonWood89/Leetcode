class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = sorted(nums)
        return new[len(new) / 2]
