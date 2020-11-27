class Solution:
    def isSymmetric(self, root):
        if not root: return True
        
        stack = [root, root]
        
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            
            if not node1 and not node2: continue
            if not node1 or not node2: return False
            if node1.val != node2.val: return False
            
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
            
        return True

class Solution2:
    def isSymmetric(self, root):
        if not root: return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, nodeLeft, nodeRight):
        if not nodeLeft and not nodeRight: return True
        if not nodeLeft or not nodeRight: return False
        if nodeLeft.val != nodeRight.val: return False
        
        return (self.isMirror(nodeLeft.left, nodeRight.right)
               and self.isMirror(nodeLeft.right, nodeRight.left))