from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        
        q = deque()
        q.append(root)
        l_to_r = True
        res = []
        
        while q:
            n = len(q)
            level = deque()
            for _ in range(n):
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