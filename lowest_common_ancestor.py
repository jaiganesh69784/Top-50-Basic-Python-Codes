class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.val == n1 or root.val == n2:
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
