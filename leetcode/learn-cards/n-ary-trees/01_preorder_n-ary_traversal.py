class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        if not root: return self.res
        self.traverse(root)
        return self.res
    
    def traverse(self, node):
        if not node: return
        self.res.append(node.val)
        for child in node.children:
            self.traverse(child)

class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])
        
        return output