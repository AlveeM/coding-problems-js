class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            n = len(matrix[0])
            r = len(matrix) - 1
            c = 0
            while r >= 0 and c < n:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    r = r - 1
                else:
                    c = c + 1
            return False
        return False
            