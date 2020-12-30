class Solution:
    def removeLeafNodes(self, root, target):
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
            
        if (root.left is root.right
            and root.val == target):
            return None
        
        return root