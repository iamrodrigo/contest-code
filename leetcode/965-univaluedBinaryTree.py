# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def isUnivalTree(self, root):
        left = root.left.val == root.val if root.left else True
        right = root.right.val == root.val if root.right else True

        if not left or not right:
            return False

        if root.left:
            left = self.isUnivalTree(root.left)

        if root.right:
            right = self.isUnivalTree(root.right)

        return left and right