class Solution:
    def isValidBST(self, root):
        if not root: return True
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, low, high):
        if not node: return True
        
        if node.val <= low or node.val >= high:
            return False
        
        left = self.helper(node.left, low, node.val)
        right = self.helper(node.right, node.val, high)
        
        return left and right