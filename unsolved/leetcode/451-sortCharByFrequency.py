from collections import Counter
from heapq import heappush, heappop

class Solution(object):
    def frequencySort(self, s):
        dictionary = Counter(s)
        heap = []

        for key, value in dictionary.iteritems():
            heappush(heap, (-value, key))

        string = ''

        for _ in xrange(len(heap)):
            element = heappop(heap)
            string += element[1] * -element[0]

        return string


s = Solution()
print s.frequencySort('aaaccc')
print s.frequencySort('tree')
print s.frequencySort('Aabb')

