from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root: return None
        
        q = deque()
        q.append(root)
        stack = []
        res = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            stack.append(level)
        
        while stack:
            res.append(stack.pop())
            
        return res