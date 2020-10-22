from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        def traverse(node):
            if not node: return node
            
            traverse(node.left)
            output.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return output

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        output = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp_node = stack.pop()
                output.append(temp_node.val)
                root = temp_node.right
            
        return output