# Binary Search Tree
def lca(root, v1, v2):
    if root.info > max(v1, v2):
        return lca(root.left, v1, v2)
    elif root.info < min(v1, v2):
        return lca(root.right, v1, v2)
    else:
        return root

# Binary Tree
# def lca(root, v1, v2):
#     if root is None: 
#         return None
#     if root.info == v1 or root.info == v2:
#         return root

#     left = lca(root.left, v1, v2)
#     right = lca(root.right, v1, v2)
#     if left and right:
#         return root
#     if left is None and right is None:
#         return None
    
#     return left or right