class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        endIdx = 0
        
        for i in range(len(nums)):
            startIdx = 0
            if i > 0 and nums[i] == nums[i-1]:
                startIdx = endIdx + 1
            
            endIdx = len(subsets) - 1
            for j in range(startIdx, endIdx+1):
                subset = subsets[j][:]
                subset.append(nums[i])
                subsets.append(subset)
                
        return subsets