class Solution:
    def generate(self, numRows):
        result = []
        
        for row in range(1, numRows+1):
            row_arr = [1] * row
            for i in range(1, row-1):
                row_arr[i] = result[row-2][i-1] + result[row-2][i]
            result.append(row_arr)
        
        return result