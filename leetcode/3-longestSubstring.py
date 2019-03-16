def lengthOfLongestSubstring(s):
    longestLength = 0
    hashTable = {}

    i = 0
    j = 0

    for c in s:
        if c in hashTable and hashTable[c] >= i and hashTable[c] <=j:
            i = hashTable[c] + 1
        hashTable[c] = j
        j += 1
        longestLength = max(longestLength, j-i)

    return longestLength


a = raw_input()
print lengthOfLongestSubstring(a)