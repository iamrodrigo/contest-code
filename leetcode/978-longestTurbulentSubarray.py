class Solution(object):

    def maxTurbulenceSize(self, A):
        turbulentSubarray = 1
        maxTurbulentSubarray = 0
        flip = False

        if len(A) == 1:
            return turbulentSubarray

        if A[1] > A[0]:
            flip = True
            turbulentSubarray += 1
        elif A[0] > A[1]:
            turbulentSubarray += 1
        else:
            turbulentSubarray = 0

        maxTurbulentSubarray = max(maxTurbulentSubarray, turbulentSubarray)

        for i in xrange(2, len(A)):
            if (A[i] > A[i - 1] and not flip) or (A[i] < A[i - 1] and flip):
                turbulentSubarray += 1
                flip = not flip
                maxTurbulentSubarray = max(maxTurbulentSubarray, turbulentSubarray)
            else:
                turbulentSubarray = 1
                flip = False
                #print A[i], A[i - 1]
                if A[i] > A[i - 1]:
                    flip = True
                    turbulentSubarray += 1
                elif A[i - 1] > A[i]:
                    turbulentSubarray += 1

        return maxTurbulentSubarray

s = Solution()
print s.maxTurbulenceSize([1, 1, 1, 1, 1])