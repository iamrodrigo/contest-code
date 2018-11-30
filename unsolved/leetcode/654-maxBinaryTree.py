class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not len(nums):
            return None
        else:
            maxInd = 0
            maxValue = nums[0]
            for i, x in enumerate(nums):
                if x > maxValue:
                    maxValue = x
                    maxInd = i

            node = TreeNode(maxValue)
            node.left = self.constructMaximumBinaryTree(nums[0:maxInd])
            node.right = self.constructMaximumBinaryTree(nums[maxInd + 1:])
            return node

s = Solution()
f = s.constructMaximumBinaryTree([1])
pass