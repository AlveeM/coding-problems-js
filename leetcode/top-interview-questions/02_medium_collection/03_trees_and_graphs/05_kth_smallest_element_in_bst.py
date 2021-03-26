class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = 0
        self.inorder(root, k)
        return self.res
    
    def inorder(self, node, k):
        if not node: return
        self.inorder(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.res = node.val
            return
        
        self.inorder(node.right, k)