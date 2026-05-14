class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = 0
        jSet = {}
        for i in range(len(jewels)):
            jSet[jewels[i]] = 1 
        
        for i in stones:
            if i in jSet:
                count += 1

        return count