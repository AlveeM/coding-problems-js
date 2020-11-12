class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp_node = stack.pop()
                res.append(temp_node.val)
                root = temp_node.right
        
        return res