# Method 1
class Solution:
    def maxAncestorDiff(self, root):
        self.maxDiff = 0
        self.dfs(root)
        return self.maxDiff
    
    def dfs(self, node):
        # (min, max)
        if node is None: return (float('inf'), float('-inf'))
        
        if node.left is None and node.right is None:
            return (node.val, node.val)
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        minVal = min(left[0], right[0])
        maxVal = max(left[1], right[1])
        
        self.maxDiff = max(self.maxDiff, max(abs(minVal-node.val), abs(maxVal-node.val)))
        
        minVal = min(minVal, node.val)
        maxVal = max(maxVal, node.val)
        
        return (minVal, maxVal)

# Method 2
class Solution2:
    def maxAncestorDiff(self, root):
        self.maxDiff = 0
        self.dfs(root, root.val, root.val)
        return self.maxDiff
        
    def dfs(self, node, low, high):
        if node is None: return
        
        absLow = abs(node.val - low)
        absHigh = abs(node.val - high)
        
        self.maxDiff = max(absLow, self.maxDiff)
        low = min(low, node.val)
        
        self.maxDiff = max(absHigh, self.maxDiff)
        high = max(high, node.val)
        
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)