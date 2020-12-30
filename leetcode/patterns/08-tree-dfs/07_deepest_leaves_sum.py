# Method 1: DFS
class Solution:
    def deepestLeavesSum(self, root):
        self.max_depth = self.maxDepth(root)
        self.sum = 0
        self.dfsSum(root)
        return self.sum
        
    def dfsSum(self, node, depth=1):
        if not node: return
        
        if depth == self.max_depth:
            self.sum += node.val
            
        self.dfsSum(node.left, depth + 1)
        self.dfsSum(node.right, depth + 1)
        
    def maxDepth(self, node):
        if not node: return 0
        
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        return max(left, right) + 1

# Method 2: BFS
class Solution2:
    def deepestLeavesSum(self, root):
        prev_nodes = []
        queue = []
        queue.append(root)
        
        while queue:
            next_nodes = []
            
            for node in queue:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            
            prev_nodes, queue = queue, next_nodes
            
        return sum(map(lambda node: node.val, prev_nodes))