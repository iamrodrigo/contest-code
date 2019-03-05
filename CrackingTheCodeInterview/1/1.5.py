from collections import Counter

def oneWay(w1, w2):
    diff = 0
    if len(w1) == len(w2):
        for i in xrange(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
            if diff > 1:
                return False
    elif abs(len(w1) - len(w2)) > 1:
        return False
    else:
        pass


    return True

print oneWay(raw_input(), raw_input())
