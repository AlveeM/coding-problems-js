class Solution:
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findPair(nums, -nums[i], i+1, triplets)
        return triplets
        
        
    def findPair(self, nums, target, l, triplets):
        r = len(nums) - 1
        
        while l < r:
            cur_sum = nums[l] + nums[r]
            
            if cur_sum == target:
                triplets.append([-target, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
                