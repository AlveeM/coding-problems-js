class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.dfs(nums, 0, len(nums)-1)
        
    def dfs(self, nums, start, end):
        if start > end: return None
        
        maxIdx = self.maxIdx(nums, start, end)
        node = TreeNode(nums[maxIdx])
        node.left = self.dfs(nums, start, maxIdx-1)
        node.right = self.dfs(nums, maxIdx+1, end)
        
        return node
        
    def maxIdx(self, arr, start, end):
        max_idx = start
        
        for i in range(start+1, end+1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        return max_idx