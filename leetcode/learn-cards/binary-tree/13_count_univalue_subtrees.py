class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
    def dfs(self, node):
        if not node:
            return
        
        if self.isUniVal(node, node.val):
            self.count += 1
        
        self.dfs(node.left)
        self.dfs(node.right)
        
    def isUniVal(self, node, val):
        if node is None: return True
        
        if (node.left is None and 
            node.right is None and 
            node.val == val):
            return True
        
        return (node.val == val and 
               self.isUniVal(node.left, val) and
               self.isUniVal(node.right, val))