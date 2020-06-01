# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = 0
        self.inOrder(root, k)
        return self.result

    def inOrder(self, root, k):
        if root.left:
            self.inOrder(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
            return
        if root.right:
            self.inOrder(root.right, k)