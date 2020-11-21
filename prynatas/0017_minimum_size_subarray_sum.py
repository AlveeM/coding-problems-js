class Solution:
    def minSubArrayLen(self, s, nums):
        # declare a variable to store window sum; initialize to 0
        window_sum = 0
        # declare a variable to store min window size; initialize to infinity
        min_size = float('inf')
        
        # declare window start idx variable; initialize it to 0
        window_start_idx = 0
        
        # iterate through nums
        for window_end_idx in range(len(nums)):
            # add current num to window sum
            window_sum += nums[window_end_idx]
            # keep decreasing the window start idx while window sum >= s
            while window_sum >= s:
                # update min size if current window < current min size
                current_window_size = window_end_idx - window_start_idx + 1
                min_size = min(min_size, current_window_size)
                # subtract element at window start idx from current sum
                window_sum -= nums[window_start_idx]
                # increment window start index by 1
                window_start_idx += 1
            
        # if min size is infinity return 0
        if min_size == float('inf'): return 0
        # return min size
        return min_size