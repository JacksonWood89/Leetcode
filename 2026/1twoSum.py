class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        info = {}
        res = []
        for i in range(len(nums)):
            info[nums[i]] = i
        for i in range(len(nums)):
            com = target - nums[i]
            if com in info and info[com] != i:
                res.append(i)
                res.append(info[com])
                return res
        return []