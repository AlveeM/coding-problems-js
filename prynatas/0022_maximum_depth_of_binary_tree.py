class Solution:
    def maxDepth(self, root):
        if not root: return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        
        return 1 + max(left_max, right_max)