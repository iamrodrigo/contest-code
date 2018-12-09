class Solution(object):
    def find2dPeakElement(self, nums):
        rows = len(nums)
        colums = len(nums[0])

        beg, end = 0, colums - 1
        j = beg + ((end - beg) / 2)

        while j >-1 and j <= colums:
            j = beg + ((end - beg) / 2)
            i = 0
            maxNum = nums[0][j]

            for q in xrange(0, rows):
                if maxNum < nums[q][j]:
                    maxNum = nums[q][j]
                    i = q

            if  (j > 0 and j < colums - 1 and nums[i][j + 1] < nums[i][j] and nums[i][j - 1] < nums [i][j]) \
                or (j == 0 and colums == 2 and nums[i][j + 1] < nums[i][j]) \
                or (j == colums - 1 and nums[i][j - 1] < nums [i][j]) \
                or (j == colums - 1):
                break
            elif nums[i][j + 1] > nums[i][j]:
                beg = j + 1
            else:
                end = j - 1

        return [i, j]

s = Solution()
print s.find2dPeakElement([[10, 8, 10, 10], [14, 13, 12, 11], [15, 9, 11, 21], [16, 17, 19, 20]])
print s.find2dPeakElement([[10, 20, 15], [21, 30, 14], [7, 16, 32]])
print s.find2dPeakElement([[10, 7], [11, 17]])  #(1, 1)
print s.find2dPeakElement([[1]])  #(1, 1)
#print s.find2dPeakElement([[]])