def stringCompression(s):
    if len(s) == 1:
        return s

    count = 0
    compressed = []

    for i in xrange(0, len(s)):

        count += 1
        if i + 1 == len(s) or s[i] != s[i + 1]:
            compressed.append(s[i] + str(count))
            count = 0

    compressedStr = ''.join(compressed)
    return compressedStr if len(compressedStr) < len(s) else s


print stringCompression('aabbbbbcdflkksgnosdfadvfeasdfdfsdfdddddfefsefddddddddddddddddddddddddddddd')

