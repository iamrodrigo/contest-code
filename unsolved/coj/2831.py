from collections import deque

a = input()
line = raw_input()
x = 0
y = 0
dicx = {0:deque()}
dicy = {0:deque()}
dicx[0].append(0)
dicy[0].append(0)
min = 0

for c in line:
    if c == 'N':
        y += 1
    elif c == 'S':
        y -= 1
    elif c == 'E':
        x += 1
    else:
        x -= 1

    if not y in dicx:
        dicx[y] = deque()
    if not x in dicy:
        dicy[x] = deque()

    if len(dicx[y]) and dicx[y][0] > x:
        dicx[y].appendleft(x)
    else:
        dicx[y].append(x)

    if len(dicy[x]) and dicy[x][0] > y:
        dicy[x].appendleft(y)
    else:
        dicy[x].append(y)

print dicx
print dicy

