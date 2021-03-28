class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        n = len(matrix[0])
        r = len(matrix) - 1
        c = 0
        
        while r >= 0 and c < n:
            num = matrix[r][c]
            if num == target:
                return True
            elif num > target:
                r = r - 1
            else:
                c = c + 1
        
        return False
            