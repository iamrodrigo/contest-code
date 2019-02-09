from collections import Counter

def oneWay(w1, w2):
    w1Char = Counter(w1)

    for c in w2:
        w1Char[c] = 1 if c not in w1Char else w1Char[c] - 1
        if w1Char[c] == 0:
            del w1Char[c]

    diff = abs(len(w1) - len(w2))
    lenW1Char = len(w1Char)

    return True if (diff == 1 and lenW1Char == 1) or (not diff and lenW1Char == 2) else False

print oneWay(raw_input(), raw_input())
