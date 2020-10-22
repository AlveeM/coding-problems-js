from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        def traverse(node):
            if not node: return node
            
            traverse(node.left)
            traverse(node.right)
            output.append(node.val)
        
        traverse(root)
        return output

class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return root
        
        stack = [root]
        stack2 = []
        
        while stack:
            node = stack.pop()
            stack2.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return stack2[::-1]
