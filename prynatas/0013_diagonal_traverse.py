class Solution:
    def findDiagonalOrder(self, matrix):
        idx_sum_dict = {}
        res = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                idx_sum = r + c
                if idx_sum in idx_sum_dict:
                    idx_sum_dict[idx_sum].append(matrix[r][c])
                else:
                    idx_sum_dict[idx_sum] = [matrix[r][c]]
                    
        for level, nums in idx_sum_dict.items():
            if level % 2 == 0:
                for num in reversed(nums):
                    res.append(num)
            else:
                for num in nums:
                    res.append(num)
                                    
        return res