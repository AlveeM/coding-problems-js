class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        visited = {}
        return self.cloneNode(node, visited)
    
    def cloneNode(self, node, visited):
        new_node = Node(node.val)
        visited[node.val] = new_node
        
        for n in node.neighbors:
            if n.val not in visited:
                cloned_node = self.cloneNode(n, visited)
                new_node.neighbors.append(cloned_node)
            else:
                new_node.neighbors.append(visited[n.val])
                
        return new_node