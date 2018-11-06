a = input()

for i in range(a):
    b = input()

    even = 0
    odd = 0

    for j in range(1, int((b ** 0.5)) + 1):
        if b%j == 0:
            if j % 2 == 0:
                even += 1
            else:
                odd += 1

            if (b/j) != j:
                if (b/j) % 2 == 0:
                    even += 1
                else:
                    odd += 1

    print "P: {} I: {}".format(even, odd)



