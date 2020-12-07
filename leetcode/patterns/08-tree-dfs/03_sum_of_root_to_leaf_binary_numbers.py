class Solution:
    def sumRootToLeaf(self, root):
        self.total = 0
        self.traverse(root, 0)
        return self.total
    
    def traverse(self, root, pathSum):
        if not root: return
        
        pathSum = (pathSum << 1) | root.val
        if root.left is None and root.right is None:
            self.total += pathSum
        else:
            self.traverse(root.left, pathSum)
            self.traverse(root.right, pathSum)