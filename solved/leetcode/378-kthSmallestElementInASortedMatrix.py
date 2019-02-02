import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        arr = []
        for x in matrix:
            arr.extend(x)

        heapq.heapify(arr)
        for i in xrange(0, k - 1):
            heapq.heappop(arr)

        return heapq.heappop(arr)