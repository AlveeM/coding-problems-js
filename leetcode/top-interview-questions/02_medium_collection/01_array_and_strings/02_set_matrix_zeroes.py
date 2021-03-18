class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        first_row_zero = False
        for col in range(COLS):
            if matrix[0][col] == 0:
                first_row_zero = True
                
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
        
        for row in range(1, ROWS):
            row_has_zero = False
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_has_zero = True
                    break
            for col in range(COLS):
                if row_has_zero or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if first_row_zero:
            for col in range(COLS):
                matrix[0][col] = 0

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_has_zero = False
        R = len(matrix)
        C = len(matrix[0])
        
        for i in range(R):
            if matrix[i][0] == 0:
                col_has_zero = True
            for j in range(1, C):
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        
        if col_has_zero:
            for i in range(R):
                matrix[i][0] = 0