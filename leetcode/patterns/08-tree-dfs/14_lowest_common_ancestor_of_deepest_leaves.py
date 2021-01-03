class Solution:
    def lcaDeepestLeaves(self, root):
        return self.dfs(root)[0]
        
    def dfs(self, node):
        '''return a tuple: (node, depth)'''
        if node is None: return (None, 0)

        left_node, left_depth = self.dfs(node.left)
        right_node, right_depth = self.dfs(node.right)

        if left_depth > right_depth:
            return (left_node, left_depth + 1)
        elif left_depth < right_depth:
            return (right_node, right_depth + 1)
        else:
            return (node, left_depth + 1)
