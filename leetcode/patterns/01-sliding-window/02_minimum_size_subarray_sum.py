# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s, nums):
        min_window_size = float('inf')
        window_sum = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= s:
                cur_window_size = window_end - window_start + 1
                min_window_size = min(min_window_size, cur_window_size)
                window_sum -= nums[window_start]
                window_start += 1
                
        if min_window_size == float('inf'):
            return 0
        
        return min_window_size