import collections

class Solution(object):
    def addStrings(self, num1, num2):

        lengthA = len(num1) - 1
        lengthB = len(num2) - 1
        sum = collections.deque()
        extra = 0

        for _ in xrange(max(lengthA, lengthB) + 1):
            c = int(num1[lengthA]) if lengthA >= 0 else 0
            d = int(num2[lengthB]) if lengthB >= 0 else 0

            total = c + d + extra
            extra = 1 if total >= 10 else 0

            sum.appendleft(str(total % 10))


            lengthA -= 1
            lengthB -= 1


        if extra:
            sum.appendleft('1')
            
        return ''.join(sum)    