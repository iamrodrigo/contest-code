a, b = map(int, raw_input().split())

c = raw_input().split()
d = raw_input().split()

if c[0] == '0':
    print 'NO'
elif c[b-1] == '1':
    print 'YES'
else:
    flag = False
    if d[b-1] == '1':
        for i in xrange(b, len(c)):
            if c[i] == '1' and d[i] == '1':
                print 'YES'
                flag = True
                break
    if not flag:
        print 'NO'