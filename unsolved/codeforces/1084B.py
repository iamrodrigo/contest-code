import math

def fairNut(kegs, l):
    smallest = kegs[-1]
    t = 0

    for keg in kegs:
        if smallest == keg:
            break
        t += keg - smallest
        if t == l:
            return smallest

    smallest = int(smallest - math.ceil((l - t) / float(len(kegs))))
    return smallest if smallest >= 0 else -1



k, l = raw_input().split()
kegs = map(int, raw_input().split())

print fairNut(sorted(kegs, reverse=True), int(l))

n, s = int(k), int(l)
a = kegs
su = sum(a)
if su < s:
    print -1
else:
    m = min(a)
    if su - m*n >= s:
        print m
    else:
        s -= su - m*n
        from math import ceil
        print int(m-ceil(float(s)/n))