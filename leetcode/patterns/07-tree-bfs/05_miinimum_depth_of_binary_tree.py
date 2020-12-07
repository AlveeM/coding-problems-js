from collections import deque

class Solution:
    def minDepth(self, root):
        if not root: return 0
        
        q = deque()
        q.append(root)
        levels = 1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return levels
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels += 1
        
        return levels