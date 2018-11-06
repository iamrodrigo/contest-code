import collections

a = raw_input()
b = raw_input()

lengthA = len(a) - 1
lengthB = len(b) - 1
sum = collections.deque()
extra = 0

for _ in xrange(max(lengthA, lengthB) + 1):
    c = int(a[lengthA]) if lengthA >= 0 else 0
    d = int(b[lengthB]) if lengthB >= 0 else 0

    total = c + d + extra
    extra = 1 if total >= 10 else 0

    sum.appendleft(str(total % 10))


    lengthA -= 1
    lengthB -= 1


if extra:
    sum.appendleft('1')

print ''.join(sum)
