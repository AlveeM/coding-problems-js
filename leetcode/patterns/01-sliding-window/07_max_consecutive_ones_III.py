# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, A, K):
        zeros = 0
        window_start = 0
        max_ones = 0
        
        for window_end in range(len(A)):
            num = A[window_end]
            
            if num == 0:
                zeros += 1
                
            if zeros > K:
                num_start = A[window_start]
                if num_start == 0:
                    zeros -= 1
                window_start += 1
                
            max_ones = max(max_ones, window_end - window_start + 1)
            
        return max_ones

class Solution2:
    def longestOnes(self, A, K):
        window_start = 0
        window_end = 0
        
        for window_end in range(len(A)):
            if A[window_end] == 0:
                K -= 1
                
            if K < 0:
                if A[window_start] == 0:
                    K += 1
                window_start += 1
                
        return window_end - window_start + 1