import math

pages, cows = map(int, raw_input().split())

for cow in range(cows):
    speed, time, rest = map(int, raw_input().split())

    T = int(math.ceil(pages / float(speed)))
    B = int(math.ceil(T / float(time)))
    B -=1
    print T+(B*rest)
