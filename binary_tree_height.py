class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_height(root):
    if root is None:
        return 0
    return max(find_height(root.left), find_height(root.right)) + 1
