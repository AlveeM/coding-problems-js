class Solution:
    def minSubArrayLen(self, s, nums):
        window_sum = 0
        min_len = float('inf')
        
        ws = 0
        for we in range(len(nums)):
            window_sum += nums[we]
            while window_sum >= s:
                min_len = min(min_len, we - ws + 1)
                window_sum -= nums[ws]
                ws += 1
        
        if min_len == float('inf'): return 0
        return min_len