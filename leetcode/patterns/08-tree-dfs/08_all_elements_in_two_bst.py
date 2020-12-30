class Solution:
    def getAllElements(self, root1, root2):
        tree1 = self.dfs(root1, [])
        tree2 = self.dfs(root2, [])
        
        if not tree1 or not tree2:
            return tree1 or tree2
        
        return self.merge(tree1, tree2)
    
    def merge(self, arr1, arr2):
        i = 0
        j = 0
        res = []
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
                
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        
        return res
        
    def dfs(self, node, res):
        if not node: return
        
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
        
        return res