class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        T = 0
        R = len(matrix[0])
        L = 0
        B = len(matrix)
        while L < R and T < B:
            for i in range(L, R): # going right from top left
                result.append(matrix[T][i])
            T += 1
            for i in range(T, B): # down from top right
                result.append(matrix[i][R - 1])
            R -= 1
            if not (L < R and T < B):
                break
            
            for i in range(R - 1, L - 1, -1):
                result.append(matrix[B - 1][i])
            B -= 1

            for i in range(B - 1, T - 1, -1):
                result.append(matrix[i][L])
            L += 1
        return result