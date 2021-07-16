# recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, nodeLeft, nodeRight):
        if not nodeLeft and not nodeRight: return True
        if not nodeLeft or not nodeRight: return False
        if nodeLeft.val != nodeRight.val: return False
        
        return (self.isMirror(nodeLeft.left, nodeRight.right)
               and self.isMirror(nodeLeft.right, nodeRight.left))

# iterative
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        q.append(root)
        
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            
            if (node1 is None and node2 is None): continue
            if (node1 is None or node2 is None): return False
            if (node1.val != node2.val): return False
        
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        
        return True
        