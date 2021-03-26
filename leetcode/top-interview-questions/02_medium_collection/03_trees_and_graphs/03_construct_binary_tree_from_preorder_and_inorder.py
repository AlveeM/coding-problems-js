class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        if n == 0: return None
        
        self.inorder = inorder
        self.preorder = preorder
        self.ino_map = {val: idx for idx, val in enumerate(inorder)}
        self.p_idx = 0
        
        return self.buildTreeRec(0, n - 1)
        
    def buildTreeRec(self, start, end):
        if start > end: return None
        
        root_val = self.preorder[self.p_idx]
        self.p_idx += 1
        root = TreeNode(root_val)
        ino_idx = self.ino_map[root_val]
        
        root.left = self.buildTreeRec(start, ino_idx - 1)
        root.right = self.buildTreeRec(ino_idx + 1, end)
        return root