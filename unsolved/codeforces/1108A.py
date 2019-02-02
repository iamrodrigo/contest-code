a = input()

for _ in xrange(a):
    q, w, e, r = map(int, raw_input().split())
    if q == e:
        print w, e
    else:
        print q, e


