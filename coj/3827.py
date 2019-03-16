a = input()
b = input()
total = 0

for i in xrange(a):
    c, d = map(int, raw_input().split())
    if abs(c - d) > b:
        total += input()
    else:
        total += max(c, d)

print total
