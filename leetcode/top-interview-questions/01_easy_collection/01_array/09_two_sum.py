class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in cache:
                return [cache[comp], idx]
            cache[num] = idx