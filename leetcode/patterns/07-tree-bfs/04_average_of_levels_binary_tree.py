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

class Solution2:
    def averageOfLevels(self, root):
        levels = []
        self.helper(root, levels, 0)

        # res = [level_obj["sum"] / level_obj["count"] for level_obj in levels]
        res = []
        for level_obj in levels:
            avg = level_obj["sum"] / level_obj["count"]    
            res.append(avg)

        return res
        
    def helper(self, node, levels, level):
        if node is None: return
        
        if level == len(levels):
            levels.append({ "sum": node.val, "count": 1 })
        else:
            levels[level]["sum"] += node.val
            levels[level]["count"] += 1
            
        self.helper(node.left, levels, level + 1)
        self.helper(node.right, levels, level + 1)