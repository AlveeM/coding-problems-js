class Solution:
    def hasPathSum(self, root, sum):
        def traverse(node, cur_sum):
            if not node:
                return False

            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == sum
            
            return traverse(node.left, cur_sum) or traverse(node.right, cur_sum)

        return traverse(root, 0)