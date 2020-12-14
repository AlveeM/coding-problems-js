class Solution:
    def fourSum(self, nums, target):
        self.res = []
        if len(nums) < 4: return self.res
        
        nums.sort()
        if nums[0] * 4 > target or nums[-1] * 4 < target: return self.res
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                self.findPair(nums, target, i, j)
                
        return self.res
    
    def findPair(self, nums, target, a_idx, b_idx):
        l = b_idx + 1
        r = len(nums) - 1
        
        while l < r:
            a, b, c, d = nums[a_idx], nums[b_idx], nums[l], nums[r]
            total = a + b + c + d
            if total == target:
                self.res.append([a, b, c, d])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1