from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        charAndFrequency = defaultdict(int)
        string = ''

        for c in s:
            charAndFrequency[c] += 1

        for e in sorted(charAndFrequency.items(), key=lambda x: x[1], reverse=True):
            string += e[0] * e[1]

        return string