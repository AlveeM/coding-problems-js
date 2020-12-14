class Solution:
    def hasPathSum(self, root, sum):
        if not root: return False
        
        new_sum = sum - root.val
        if not root.left and not root.right: 
            return new_sum == 0
        
        return (self.hasPathSum(root.left, new_sum)
               or self.hasPathSum(root.right, new_sum))
