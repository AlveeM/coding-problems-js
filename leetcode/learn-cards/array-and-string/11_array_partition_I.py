class Solution:
    def arrayPairSum(self, nums):
        nums_sorted = sorted(nums)
        max_sum = 0
        for i in range(0, len(nums)-1, 2):
            max_sum += nums_sorted[i]

        return max_sum