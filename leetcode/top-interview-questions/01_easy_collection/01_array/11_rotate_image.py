class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # top_left = matrix[i][j]
        # top_right = matrix[j][n-i-1]
        # bottom_right = matrix[n-i-1][n-j-1]
        # bottom_left = matrix[n-1-j][i]
        
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                top_left_val = matrix[i][j]
                
                # top left <- bottom left
                matrix[i][j] = matrix[n-1-j][i]
                
                # bottom left <- bottom right
                matrix[n-1-j][i] = matrix[n-i-1][n-j-1] 
                
                # bottom right <- top right
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                
                # top right <- top left
                matrix[j][n-i-1] = top_left_val