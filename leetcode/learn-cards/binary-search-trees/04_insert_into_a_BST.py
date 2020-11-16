class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root

# iterative
class Solution2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if not root: return new_node
        
        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = new_node
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_node
                    return root
                cur = cur.right