from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(mat) * len(mat[0]) != r * c:
            return mat

        res = [[0] * c for _ in range(r)]

        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                nums.append(mat[i][j])

        pos = 0
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = nums[pos]
                pos += 1

        return res

s = Solution()
assert s.matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
assert s.matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]
assert s.matrixReshape([[1,2],[3,4]], 4, 1) == [[1],[2],[3],[4]]
print("All tests passed")