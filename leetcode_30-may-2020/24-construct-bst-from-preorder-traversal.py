from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.build_tree(preorder, 0, len(preorder) - 1)

    def build_tree(self, preorder, l, r):
        if (l > r):
            return None

        root = TreeNode(preorder[l])
        if (l == r):
            return root

        idx = l + 1
        while (idx <= r and preorder[idx] < preorder[l]):
            idx += 1

        root.left = self.build_tree(preorder, l+1, idx-1)
        root.right = self.build_tree(preorder, idx, r)

        return root