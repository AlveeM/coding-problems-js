from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque()

        if root:
            q.append(root)

        while len(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

# DFS
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root, level, res):
        if root is None: return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)