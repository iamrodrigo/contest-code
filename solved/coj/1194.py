grid = {}

a = raw_input()
b = raw_input()

for i in a[7:].split(','):
    if len(i) == 3:
        grid[i[1:]] = i[0]
    else:
        grid[i] = 'P'

for i in b[7:].split(','):
    if len(i) == 3:
        grid[i[1:]] = i[0].lower()
    else:
        grid[i] = 'p'

for i in xrange(17, 0, -1):
    if i % 2 != 0:
        print "+---+---+---+---+---+---+---+---+"
    else:
        c = 97
        dot = '.' if (i/2) % 2 == 0 else ':'
        row = []
        for j in xrange(8):
            row.append("|"+dot)
            row.append(grid[chr(c)+str(i/2)] if chr(c)+str(i/2) in grid else dot)
            row.append(dot)
            dot = '.' if dot == ':' else ':'
            c += 1
        print "".join(row)+"|"


