class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
# Method 1: in-order traversal and queue to store nodes
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.roots = deque()
        self._traverse(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.roots.popleft()
        return cur
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.roots) != 0
        
    def _traverse(self, root):
        if not root: return 
        self._traverse(root.left)
        self.roots.append(root.val)
        self._traverse(root.right)

# Method 2: in-order traversal without queue
class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._traverse_left_nodes(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top_node = self.stack.pop()
        if top_node.right:
            self._traverse_left_nodes(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        
    def _traverse_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left