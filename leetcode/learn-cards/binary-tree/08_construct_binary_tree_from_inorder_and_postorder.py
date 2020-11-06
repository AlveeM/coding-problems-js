class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        n = len(inorder)
        if n == 0: return None
            
        self.inorder = inorder
        self.postorder = postorder
        self.io_dict = {val: idx for idx, val in enumerate(inorder)}
            
        return self.buildTreeRec(0, n, 0, n)
    
    def buildTreeRec(self, i1, i2, p1, p2):
        if i1 >= i2 or p1 >= p2: return None
        
        root_val = self.postorder[p2-1]
        root = TreeNode(root_val)
        root_idx = self.io_dict[root_val]
        offset = root_idx - i1
        
        root.left = self.buildTreeRec(i1, i1 + offset, p1, p1 + offset)
        root.right = self.buildTreeRec(i1 + offset + 1, i2, p1 + offset, p2 - 1)
        
        return root

class Solution2:
    def buildTree(self, inorder, postorder):
        io_dict = {val: idx for idx, val in enumerate(inorder)}
        
        def buildTreeRecur(low, high):
            if low > high: return None
            
            root = TreeNode(postorder.pop())
            mid = io_dict[root.val]
            root.right = buildTreeRecur(mid + 1, high)
            root.left = buildTreeRecur(low, mid - 1)
            
            return root
        
        return buildTreeRecur(0, len(postorder) - 1)