import math

a = input()
for _ in xrange(0, a):
    bookSize, startPage, endPage, jumpsAllowed = map(int, raw_input().split())
    jumps = abs(((endPage - startPage) / float(jumpsAllowed)))

    if jumps.is_integer():
        print int(jumps)
        continue

    jumpsLeft = abs(math.ceil(((startPage - 1) / float(jumpsAllowed)))) + abs((endPage - 1) / float(jumpsAllowed))
    jumpsRight = abs(math.ceil(((bookSize - startPage) / float(jumpsAllowed)))) + abs((bookSize - endPage) / float(jumpsAllowed))

    if jumpsLeft.is_integer() and jumpsRight.is_integer():
        print min(int(jumpsLeft), int(jumpsRight))
    elif jumpsLeft.is_integer():
        print int(jumpsLeft)
    elif jumpsRight.is_integer():
        print int(jumpsRight)
    else:
        print -1