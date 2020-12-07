from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root: return None
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            total = 0
            count = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(total / count)
            
        return res