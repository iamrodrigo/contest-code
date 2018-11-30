def generateMatrix(n):
    """
            :type n: int
            :rtype: List[List[int]]
            """

    # initialize
    r = [[0 for _ in range(n)] for _ in range(n)]

    # movement delta
    d = n - 1

    # current number
    i = 1

    # current row and column
    row = 0
    col = 0

    while d > 0:

        # right
        for _ in range(d):
            r[row][col] = i
            col += 1
            i += 1

        # down
        for _ in range(d):
            r[row][col] = i
            row += 1
            i += 1

        # left
        for _ in range(d):
            r[row][col] = i
            col -= 1
            i += 1

        # up
        for _ in range(d):
            r[row][col] = i
            row -= 1
            i += 1

        # resolve over shoot
        row += 1
        col += 1

        # next delta
        d -= 2

    # add middle if odd
    if n % 2 != 0:
        r[row][col] = i

    # return
    return r

def generateMatrixII(n):
    arrays = [[0 for h in xrange(n)] for i in xrange(n)]

    k = n
    m = 1
    count = 1
    array = 0
    square = n ** 2
    pointer = -1

    while m <= square:
        for z in xrange(0, k):
            pointer = pointer + 1
            arrays[array][pointer] = m
            m = m + 1

        count = count + 1
        if count == 2:
            count = 0
            k = k - 1

        for x in xrange(0, k):
            array = array + 1
            arrays[array][pointer] = m
            m = m + 1

        count = count + 1
        if count == 2:
            count = 0
            k = k - 1

        for x in xrange(0, k):
            pointer = pointer - 1
            arrays[array][pointer] = m
            m = m + 1

        count = count + 1
        if count == 2:
            count = 0
            k = k - 1

        for x in xrange(0, k):
            array = array - 1
            arrays[array][pointer] = m
            m = m + 1

        count = count + 1
        if count == 2:
            count = 0
            k = k - 1

    return arrays

def generateMatrixIII(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n * n):
        A[i][j] = k + 1
        if A[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A

a = input()
#print generateMatrix(a)
#print generateMatrixII(a)
print generateMatrixIII(a)