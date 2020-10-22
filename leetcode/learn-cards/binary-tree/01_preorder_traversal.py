from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(node):
            if not node: return node
            output.append(node)
            output.append(self.preorderTraversal(node.left))
            output.append(self.preorderTraversal(node.right))

        traverse(root)
        return output

class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return None
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output