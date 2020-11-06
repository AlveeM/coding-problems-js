class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        n = len(inorder)
        if n == 0: return None
        
        self.inorder = inorder
        self.preorder = preorder
        self.io_dict = {val: idx for idx, val in enumerate(inorder)}
        self.p_idx = 0
        
        return self.buildTreeRec(0, n-1)
    
    def buildTreeRec(self, start, end):
        if start > end: return None
        
        root_val = self.preorder[self.p_idx]
        self.p_idx += 1
        root = TreeNode(root_val)
        io_idx = self.io_dict[root_val]
        
        root.left = self.buildTreeRec(start, io_idx-1)
        root.right = self.buildTreeRec(io_idx+1, end)
        return root
        