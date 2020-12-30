class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node: return 0
        
        left_sum = max(self.dfs(node.left), 0)
        right_sum = max(self.dfs(node.right), 0)
        cur_sum = left_sum + right_sum + node.val
        
        self.max_sum = max(self.max_sum, cur_sum)
        
        return max(left_sum, right_sum) + node.val