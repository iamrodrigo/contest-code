# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution(object):
    def mergeTrees(self, t1, t2):
            if not t1 and not t2:
                return None
            elif not t1:
                return t2
            elif not t2:
                return t1

            t1.val += t2.val    
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)

            return t1


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

s = Solution()
p = s.mergeTrees(root, root2)
pass