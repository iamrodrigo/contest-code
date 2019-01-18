from heapq import nlargest
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        mostFrequentElements = defaultdict(int)

        for n in nums:
            mostFrequentElements[n] += 1

        print nlargest(k, mostFrequentElements.keys(), key=mostFrequentElements.get())
