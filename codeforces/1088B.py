from collections import deque

n, k = map(int, raw_input().split())
list = map(int, raw_input().split())
list.sort()
q = deque(list)
del list
total = 0

for _ in xrange(0, k):
    e = 0
    while len(q):
        q[0] -= total
        e = q[0]
        q.popleft()

        if e > 0:
            total += e
            break

    print e