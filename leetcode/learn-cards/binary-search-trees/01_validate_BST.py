class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isValidRec(root, float('-inf'), float('inf'))

    def isValidRec(self, root, low, high):
        if not root: return True
        
        if root.val <= low or root.val >= high:
            return False
        
        return self.isValidRec(root.left, low, root.val) and self.isValidRec(root.right, root.val, high)

# in-order traversal should have increasing elements for valid BST
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        val = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= val:
                return False
            val = root.val
            root = root.right
            
        return True