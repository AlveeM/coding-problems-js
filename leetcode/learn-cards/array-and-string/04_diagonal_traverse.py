from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix):
        idx_sum = defaultdict(list)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                idx_sum[i+j].append(matrix[i][j])
        
        result = []
        for level, values in idx_sum.items():
            if level % 2 == 0:
                for val in reversed(values):
                    result.append(val)
            else:
                for val in values:
                    result.append(val)
                    
        return result