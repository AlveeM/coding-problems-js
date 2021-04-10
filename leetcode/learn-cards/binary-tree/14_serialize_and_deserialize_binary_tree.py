from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None: return "X,"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return str(root.val) + "," + left + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")[0:-1]
        nodes_left = deque()
        for val in data:
            nodes_left.append(val)
        
        def helper(nodes):
            val = nodes.popleft()
            
            if val == "X": 
                return None
            
            node = TreeNode(int(val))
            node.left = helper(nodes)
            node.right = helper(nodes)
            
            return node
            
        return helper(nodes_left)