class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        if not root: return self.res
        self.traverse(root)
        return self.res
    
    def traverse(self, node):
        if not node: return 
        
        for child in node.children:
            self.traverse(child)
        
        self.res.append(node.val)

class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root: return res
        
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
            for child in node.children:
                stack.append(child)
                
        return res[::-1]

class Solution3:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        res = []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            for child in node.children:
                stack1.append(child)
        
        while stack2:
            val = stack2.pop().val
            res.append(val)
        
        return res