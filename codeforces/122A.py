import itertools

uglyNumbers = {int(x+y+z) for x,y,z in itertools.product(['0','4','7'], repeat=3) if z != '0'}

a = input()

answer = ""

if a in uglyNumbers:
    answer = "YES"
else:
    for n in uglyNumbers:
        if a % n == 0:
            answer = "YES"
            break

    if not answer:
        answer = "NO"

print answer