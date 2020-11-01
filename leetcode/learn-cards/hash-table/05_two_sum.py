class Solution:
    def twoSum(self, nums, target):
        cache = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in cache:
                return [cache[complement], i]
            cache[nums[i]] = i