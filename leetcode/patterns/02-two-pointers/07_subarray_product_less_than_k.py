class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        count = 0
        product = 1
        window_start = 0
        
        for window_end in range(len(nums)):
            product *= nums[window_end]
            while window_start < window_end and product >= k:
                product /= nums[window_start]
                window_start += 1
            if product < k:
                count += window_end - window_start + 1
                
        return count