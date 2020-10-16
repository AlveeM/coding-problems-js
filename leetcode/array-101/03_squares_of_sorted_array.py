from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        result = [0 for x in range(n)]
        
        highest_idx = n - 1
        left_idx = 0
        right_idx = n - 1
        
        while left_idx <= right_idx: 
            lsquare = A[left_idx] ** 2
            rsquare = A[right_idx] ** 2
            
            if lsquare > rsquare:
                result[highest_idx] = lsquare
                left_idx += 1
            else:
                result[highest_idx] = rsquare
                right_idx -= 1
                
            highest_idx -= 1
            
        return result