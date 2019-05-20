class Solution(object):
    def multiply(self, num1, num2):


        c = [0] * (len(num1) + len(num2))
        for j in xrange(len(num2) - 1, -1, -1):
            for i in xrange(len(num1) - 1, -1, -1):
                curr = (i + j) + 1
                c[curr] += (int(num1[i]) * int(num2[j]))

                units = c[curr] % 10
                dec = (c[curr] - units) / 10

                c[curr] = units
                c[curr - 1] += dec

        result =  ''.join([str(x) for x in c]).lstrip("0")

        return result if result != "" else "0"


s = Solution()
print s.multiply("2", "0")