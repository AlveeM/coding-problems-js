# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root: return None
        
        # create a queue
        queue = deque()
        # enque the root
        queue.append(root)
        # declare a variable to store level arrays (result)
        result = []
        
        # loop while queue is not empty
        while queue:
            # declare a variable to store level values (level)
            level = []
            # for each node in queue
            for _ in range(len(queue)):
                # deque the node
                node = queue.popleft()
                # append the node value to level
                level.append(node.val)
                # if there's a left node
                if node.left:
                    # enqueue the left node
                    queue.append(node.left)
                # if there's a right node
                if node.right:
                    # enqueue the right node
                    queue.append(node.right)

            # append level to result
            result.append(level)
        
        # return result
        return result