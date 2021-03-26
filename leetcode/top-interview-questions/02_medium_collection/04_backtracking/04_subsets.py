class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, [], nums)
        return self.res
    
    def backtrack(self, start, path, nums):
        self.res.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(i + 1, path, nums)
            path.pop()