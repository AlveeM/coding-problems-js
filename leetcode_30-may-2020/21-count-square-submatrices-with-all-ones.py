from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        counts = [0] * n
        top_left = 0
        result = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    top = 0 if i == 0 else counts[j]
                    left = 0 if j == 0 else counts[j-1]
                    counts[j] = 1 + min(top, left, top_left)
                    result += counts[j]

                    top_left = 0 if j == n-1 else top
                else:
                    counts[j] = 0

        return result