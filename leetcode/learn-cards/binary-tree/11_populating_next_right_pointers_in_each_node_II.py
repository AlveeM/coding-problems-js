from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        q = deque()
        q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(level) - 1):
                level[i].next = level[i+1]
        
        return root
