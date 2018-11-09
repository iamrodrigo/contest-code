class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True

        if root.left and root.left.val > root.val or root.right and root.right.val < root.val:
            return False

        leftFlag = self.isValidBST(root.left)
        rightFlag = self.isValidBST(root.right)

        return leftFlag and rightFlag

s = Solution()
s.isValidBST()
