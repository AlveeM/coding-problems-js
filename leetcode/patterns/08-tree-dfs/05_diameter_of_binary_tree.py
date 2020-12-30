class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, node):
        if not node: return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.diameter = max(self.diameter, left + right)
        
        return 1 + max(left, right)