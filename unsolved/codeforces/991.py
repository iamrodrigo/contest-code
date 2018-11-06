import math

a = input()
dict = {2: 0, 3: 0, 4:0, 5: 0}

for x in raw_input().split():
    dict[int(x)] += 1

total = dict[2] * 2 + dict[3] * 3 + dict[4] * 4 + dict[5] * 5
expected = int(math.ceil(4.5 * a))
remaining = expected - total


if remaining <= 0:
    modify = 0
else:
    min = 2
    modify = 0
    while min <= 5:
        if dict[min] >= 1:
            dict[min] -=1
            modify += 1
            remaining -= (5 - min)
            if remaining <= 0:
                break
        else:
            min += 1

print modify