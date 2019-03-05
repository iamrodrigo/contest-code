class Solution(object):
    def rotate(self, matrix):
        length = len(matrix[0]) - 1

        if not length:
            return

        for i in xrange(0, (length / 2) + 1):
            for j in xrange(i, length - i):
                a = matrix[i][j]
                b = matrix[j][length - i]
                c = matrix[length - i][length - j]
                d = matrix[length - j][i]

                matrix[i][j] = d
                matrix[j][length - i] = a
                matrix[length - i][length - j] = b
                matrix[length - j][i] = c

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])