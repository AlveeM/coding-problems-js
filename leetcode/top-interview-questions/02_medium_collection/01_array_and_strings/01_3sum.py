class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        
        triplets = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums, i+1, -nums[i], triplets)
        
        return triplets
    
    def twoSum(self, nums, l, target, triplets):
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
            