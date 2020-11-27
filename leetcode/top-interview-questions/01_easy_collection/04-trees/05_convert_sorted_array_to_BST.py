class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        return self.traverse(nums, 0, len(nums)-1)
    
    def traverse(self, arr, start, end):
        if end < start: return None
        
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        root.left = self.traverse(arr, start, mid-1)
        root.right = self.traverse(arr, mid+1, end)
        
        return root