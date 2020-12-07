class Solution:
    def pathSum(self, root, sum):
        return self.traverse(root, sum, [])
    
    def traverse(self, node, target, path):
        if node is None: return 0
        
        path.append(node.val)
        pathSum = 0
        pathCount = 0
        for i in range(len(path)-1, -1, -1):
            pathSum += path[i]
            if pathSum == target:
                pathCount += 1
        
        pathCount += self.traverse(node.left, target, path)
        pathCount += self.traverse(node.right, target, path)
        
        path.pop()
        return pathCount

class Solution2:
    def pathSum(self, root, sum):
        self.count = 0
        self.cache = {0: 1}
        self.dfs(root, 0, sum)
        return self.count
    
    def dfs(self, node, cur_sum, sum):
        if not node: return
        
        cur_sum += node.val
        if cur_sum - sum in self.cache:
            self.count += self.cache[cur_sum - sum]
        
        self.cache[cur_sum] = self.cache.get(cur_sum, 0) + 1
        
        self.dfs(node.left, cur_sum, sum)
        self.dfs(node.right, cur_sum, sum)
        
        self.cache[cur_sum] -= 1