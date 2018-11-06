import math

a = input()
nums = [int(i) for i in raw_input().split()]
total = sum(nums)
expected = int(math.ceil(4.5 * a))
remaining = expected - total


if remaining <= 0:
    print 0
else:
    modify = 0
    nums.sort()
    for n in nums:
        modify += 1
        remaining -= (5 - n)
        if remaining <= 0:
            break

    print modify
