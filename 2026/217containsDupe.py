class Solution:
    def containsDuplicate(self, nums):

        track = {}

        for i in nums:
            if i in track:
                return True
            else:
                track[i] = 1
        
        return False
