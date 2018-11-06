class Solution(object):
    def maxSubarraySumCircular(self, A):
        maxSum = A[0]
        tempMaxSum = 0
        for d in A:
            tempMaxSum += d
            if tempMaxSum < 0:
                tempMaxSum = 0

            maxSum = max(maxSum, tempMaxSum)

        for d in A:
            tempMaxSum += d

            if tempMaxSum < maxSum:
                break
            else:
                maxSum += tempMaxSum

        return maxSum


s = Solution()
print s.maxSubarraySumCircular([1,-2,3,-2])
print s.maxSubarraySumCircular([5,-3,5])
print s.maxSubarraySumCircular([3,-1,2,-1])
print s.maxSubarraySumCircular([3,-2,2,-3])
print s.maxSubarraySumCircular([-2,-3,-1])

