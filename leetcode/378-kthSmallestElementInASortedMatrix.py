class Solution(object):
    def kthSmallest(self, matrix, k):
        arr = []
        for x in matrix:
            arr.extend(x)

        arr.sort()
        return arr[k - 1]