class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_copy = nums.copy()
        
        for i in range(n):
            new_idx = (i + k) % n
            nums[new_idx] = nums_copy[i]

class Solution2:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1