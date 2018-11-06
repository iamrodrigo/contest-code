a = input()

for i in range(a):
  b, c = map(int, raw_input().split())
  d = c - b + 1
  e = d // 2
  f = d - e

  if d % 2 == 0 or b % 2 != 0:
    print str(e) + " " + str(f)
  else:
    print str(f) + " " + str(e)