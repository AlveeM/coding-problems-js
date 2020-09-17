class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.pX = 0
        self.pY = 0
        self.dX = -1
        self.dY = -1
        self.parent_and_depth(root, x, y, 0)
        return (self.dX == self.dY) and (self.pX != self.pY)

    def parent_and_depth(self, root, x, y, d):
        if root is None: return

        if root.left is not None:
            if root.left.val == x:
                self.pX = root.val
                self.dX = d + 1
            elif root.left.val == y:
                self.pY = root.val
                self.dY = d + 1

        if root.right is not None:
            if root.right.val == x:
                self.pX = root.val
                self.dX = d + 1
            elif root.right.val == y:
                self.pY = root.val
                self.dY = d + 1

        if (self.dX!= -1) and (self.dY != -1): return
        self.parent_and_depth(root.left, x, y, d + 1)
        self.parent_and_depth(root.right, x, y, d + 1)
