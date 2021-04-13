class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        self.max_depth = 1
        self.traverse(root, 1)
        return self.max_depth
    
    def traverse(self, node, depth):
        if not node: return 
        
        self.max_depth = max(depth, self.max_depth)
        for child in node.children:
            self.traverse(child, depth + 1)

class Solution2:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        stack = []
        stack.append((1, root))
        depth = 0
        
        while stack:
            cur_depth, node = stack.pop()
            if node:
                depth = max(cur_depth, depth)
                for child in node.children:
                    stack.append((cur_depth + 1, child))
                    
        return depth