n, x, y = map(int, raw_input().split())
d = list(map(int, raw_input().split()))

if x > y:
    print n
else:
    d.sort()
    brokenDoors = 0
    for i in xrange(0, len(d), 2):
        if d[i] - x > 0:
            break
        else:
            brokenDoors += 1

    print brokenDoors

