from collections import deque

class Solution:
    def openLock(self, deadends, target):
        depth = -1
        visited = set(deadends)
        q = deque(['0000'])
        
        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target: return depth
                if cur not in visited:
                    visited.add(cur)
                    q.extend(self.next_combinations(cur))
        
        return -1
                
    def next_combinations(self, combination):
        res = []
        for i, digit in enumerate(combination):
            num = int(digit)
            up = combination[:i] + str((num + 1) % 10) + combination[i+1:]
            down = combination[:i] + str((num - 1) % 10) + combination[i+1:]
            res.extend([up, down])
        return res