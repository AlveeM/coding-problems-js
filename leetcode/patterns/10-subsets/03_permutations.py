class Solution:        
    def permute(self, nums):
        self.res = []
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, nums, path):
        if len(nums) == len(path):
            self.res.append(path[:])
            return
        
        for num in nums:
            if num in path:
                continue
            
            path.append(num)
            self.backtrack(nums, path)
            path.pop()

class Solution2:
    def permute(self, nums):
        self.res = []
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]])