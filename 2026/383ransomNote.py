class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterbank = {}
        
        for i in magazine:
            if i in letterbank:
                letterbank[i] += 1
            else:
                letterbank[i] = 1

        for i in ransomNote:
            if i in letterbank and letterbank[i] > 0:
                letterbank[i] -= 1
            else:
                return False
        
        return True