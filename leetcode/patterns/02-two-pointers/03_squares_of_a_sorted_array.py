class Solution:
    def sortedSquares(self, A):
        res = [0] * len(A)
        max_idx = len(res) - 1
        l = 0
        r = max_idx
        
        while l <= r: 
            num_l = A[l] ** 2
            num_r = A[r] ** 2
            
            if num_l > num_r:
                res[max_idx] = num_l
                l += 1
            else:
                res[max_idx] = num_r
                r -= 1
            
            max_idx -= 1
                
        return res