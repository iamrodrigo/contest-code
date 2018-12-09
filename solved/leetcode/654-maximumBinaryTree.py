# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, arr):
        stack = []
        for num in arr:
            cur = TreeNode(num)
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]

s = Solution()
s.constructMaximumBinaryTree([9, 8, 7, 6, 10])