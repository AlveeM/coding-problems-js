from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return None
        
        q = deque()
        q.append(root)
        res = []
        l_to_r = True
        
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                
                if l_to_r:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                        
            res.append(level)
            l_to_r = not l_to_r
            
        return res

from collections import deque

class Solution2:
    def zigzagLevelOrder(self, root):
        if not root: return None
        
        q = deque()
        q.append(root)
        direction = 1
        res = []
        
        while q:
            level = [node.val for node in list(q)[::direction]]

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level)
            direction *= -1
            
        return res