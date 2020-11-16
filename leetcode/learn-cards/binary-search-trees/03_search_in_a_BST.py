class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        while root:
            if val == root.val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        
        return None

# iterative
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
                
        return None