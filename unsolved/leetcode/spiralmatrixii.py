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

print generateMatrix(input())