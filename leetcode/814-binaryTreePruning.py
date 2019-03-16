# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        if not root:
            return root
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        return root if root.val or root.left or root.right else None
        
        