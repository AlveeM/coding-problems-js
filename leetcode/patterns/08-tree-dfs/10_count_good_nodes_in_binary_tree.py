class Solution:
    def goodNodes(self, root):
        self.count = 0
        self.dfs(root)
        return self.count
    
    def dfs(self, node, maxVal=float('-inf')):
        if not node: return 
        
        if node.val >= maxVal:
            self.count += 1
            maxVal = node.val
            
        self.dfs(node.left, maxVal)
        self.dfs(node.right, maxVal)