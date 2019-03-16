class Solution(object):
    def isValidSerialization(self, preorder):
        nodes = 1
        for node in preorder.split(','):
            nodes = nodes - 1 if node == '#' else nodes + 1
            if nodes < 0:
                return False

        return False if nodes != 0 else True

s = Solution()
print s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print s.isValidSerialization("1,#")
print s.isValidSerialization("9,#,#,1")
print s.isValidSerialization("1,#,#,#,#")