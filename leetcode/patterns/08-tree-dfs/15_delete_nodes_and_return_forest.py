class Solution:
    def delNodes(self, root, to_delete):
        self.nodes = []
        self.toDelete = set(to_delete)
        self.delNodesRec(root)
        
        if not root.val in self.toDelete:
            self.nodes.append(root)
            
        return self.nodes
        
    def delNodesRec(self, node):
        if node is None: return None
        
        node.left = self.delNodesRec(node.left)
        node.right = self.delNodesRec(node.right)
        
        if node.val in self.toDelete:
            if node.left is not None:
                self.nodes.append(node.left)
            if node.right is not None:
                self.nodes.append(node.right)
            return None

        return node