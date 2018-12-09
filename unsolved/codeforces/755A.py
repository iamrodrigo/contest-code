cribe = [1 for _ in xrange(0, 9998)]

for i in xrange(2, 10000):
    if not cribe[i - 2]:
        continue
    for j in xrange(i * 2, 10000, i):
        cribe[j - 2] = 0

a = input()

for i in xrange(1, 10000):
    if not cribe[(a * i + 1) - 2]:
        print i
        break