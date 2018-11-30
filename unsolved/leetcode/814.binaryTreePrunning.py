class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        if not root:
            return root

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        return root if root.val == 1 or (root.left and root.left.val == 1) or (
                    root.right and root.right.val == 1) else None

