from collections import deque

def validate(x, y):
    possible1 = abs(queen[0] - x)
    possible2 = abs(queen[1] - y)

    if x >= len(matrix) or x < 0 or y >= len(matrix[0]) or y < 0 or matrix[x][y] == -1 or not possible1 or not possible2 or \
            [queen[0] + possible1, queen[1] + possible1] == [x, y] or [queen[0] + possible1, queen[1] - possible1] == [x, y] or \
            [queen[0] - possible1, queen[1] + possible1] == [x, y] or [queen[0] - possible1, queen[1] - possible1] == [x, y] or \
            [queen[0] + possible2, queen[1] + possible2] == [x, y] or [queen[0] + possible2, queen[1] - possible2] == [x, y] or \
            [queen[0] - possible2, queen[1] + possible2] == [x, y] or [queen[0] - possible2, queen[1] - possible2] == [x, y]:
        return False

    if matrix[x][y] != -2:
        esmatrix[x][y] = -2

    return True

def kingEscape():

    while q:
        p = q.popleft()
        matrix[p[0]][p[1]] = -1

        if p == destination:
            return True

        validate(p[0] + 1, p[1] - 1)
        validate(p[0] + 1, p[1])
        validate(p[0] + 1, p[1] + 1)
        validate(p[0], p[1] + 1)
        validate(p[0] - 1, p[1] + 1)
        validate(p[0] - 1, p[1])
        validate(p[0] - 1, p[1] - 1)
        validate(p[0], p[1] - 1)

    return False

n = input()
matrix = [[0 for _ in xrange(0, n)] for _ in xrange(0, n)]

queen = map(int, raw_input().split())
queen[0], queen[1] = n - queen[1], queen[0] -1

king = map(int, raw_input().split())
king[0], king[1] = n - king[1], king[0] -1

destination = map(int, raw_input().split())
destination[0], destination[1] = n - destination[1], destination[0] -1

q = deque([king])

print 'YES' if kingEscape() else 'NO'