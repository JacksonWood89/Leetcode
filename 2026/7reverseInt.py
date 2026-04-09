class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        result = 0
        while x > 0:
            result *= 10
            result += x % 10
            x = x // 10
        if result > 2 ** 31 - 1:
            return 0
        if negative:
            return result * -1
        return result