def checkBST(root):
    def helper(root, min_data, max_data):
        if root is None:
            return True
        if root.data <= min_data or root.data >= max_data:
            return False
        return (helper(root.left, min_data, root.data)
                and helper(root.right, root.data, max_data))

    return helper(root, float('-inf'), float('inf'))