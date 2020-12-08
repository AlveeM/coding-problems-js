class Solution:
    def subsets(self, nums):
        subsets = [[]]
        for num in nums:
            n = len(subsets)
            for i in range(n):
                subsets.append(subsets[i].copy() + [num])
        return subsets