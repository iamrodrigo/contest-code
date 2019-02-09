def repeatedChar(word):
    if len(word) > 1:
        word = sorted(word)
        p = word[0]
        for i in xrange(1, len(word)):
            if p == word[i]:
                return 'YES ' + p
            p = word[i]
    return 'NO'


print repeatedChar(raw_input())





