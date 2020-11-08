class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        # 0: right, 1: bottom, 2: left, 3: up
        direction = 0
        
        # initial pointers
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1 
        
        # traverse and append to result
        result = []
        while top <= bottom and left <= right:
            if direction == 0:
                for c in range(left, right+1):
                    result.append(matrix[top][c])
                top += 1
            if direction == 1:
                for r in range(top, bottom+1):
                    result.append(matrix[r][right])
                right -= 1
            if direction == 2:
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            if direction == 3:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                left += 1
            
            direction = (direction + 1) % 4
            
        return result