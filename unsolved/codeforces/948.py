from collections import deque

def checkPoint(i, j, q):
    if i >= len(matrixB) or i < 0 or j >= len(matrixB[0]) or j < 0:
        return True
    elif matrixB[i][j] == 'S' and not matrixA[i][j]:
        matrixA[i][j] = 1
        q.append((i, j))
    elif matrixB[i][j] == '.':
        matrixB[i][j] = 'D'
    elif matrixB[i][j] == 'W':
        return False

    return True

def iterateMatrix():
    for i in xrange(0, r):
        for j in xrange(0, c):
            if matrixB[i][j] == 'S':
                matrixA[i][j] = 1

                q = deque([(i, j)])

                while q:
                    point = q.popleft()

                    if not (
                        checkPoint(point[0] + 1, point[1], q) and
                        checkPoint(point[0] - 1, point[1], q) and
                        checkPoint(point[0], point[1] + 1, q) and
                        checkPoint(point[0], point[1] - 1, q)
                        ):
                        print 'No'
                        return False

    print 'Yes'
    for i in matrixB:
        print ''.join(i)

r, c = map(int, raw_input().split())

matrixA = [[0 for _ in xrange(0, c)] for _ in xrange(0, r)]
matrixB = [list(raw_input()) for _ in xrange(0, r)]
iterateMatrix()
