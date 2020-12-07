class Solution:
    def pathSum(self, root, sum):
        self.res = []
        self.traverse(root, sum, [])
        return self.res
    
    def traverse(self, root, sum, path):
        if not root: return 
        
        sum -= root.val
        path.append(root.val)
        if not root.left and not root.right and sum == 0:
            self.res.append(path.copy())
        else:
            self.traverse(root.left, sum, path)
            self.traverse(root.right, sum, path)
        path.pop()