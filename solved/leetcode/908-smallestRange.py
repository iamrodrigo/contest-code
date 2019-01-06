class Solution(object):
    def smallestRangeI(self, A, K):
        minValue = A[0]
        maxValue = A[0]
        for a in A:
            minValue = min(a, minValue)
            maxValue = max(a, maxValue)

        smallest = (maxValue - K) - (minValue + K)

        return 0 if smallest < 0 else smallest