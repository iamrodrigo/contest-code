class Solution(object):
    def minIncrementForUnique(self, A):
        if not len(A):
            return 0

        unique = set()
        A.sort()
        increment = 0
        lastVal = A[0]

        for i, a in enumerate(A):
            if a in unique:
                newVal = lastVal + 1
                increment += newVal - a
                a = newVal
            unique.add(a)
            lastVal = a

        return increment