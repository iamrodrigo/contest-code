import math

def superpalindrone(l, r):
    count = 0
    sqrtl = int(math.ceil(math.sqrt(l)))
    sqrtr = int(math.ceil(math.sqrt(r)))


    for i in xrange(sqrtl,sqrtr+1):
        j = str(i)
        if j[0] == j[-1]:
            k = i * i
            l = str(int(k))
            if l[0] == l[-1]:
                count += 1

    return count


print superpalindrone(1, 1000000000000000000)
