class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.inorder_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.inorder_successor(root)
                root.right = self.deleteNode(root.right, root.val)
                
        return root
                
    def inorder_predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def inorder_successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val