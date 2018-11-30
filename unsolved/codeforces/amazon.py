import collections

def recursion(x, y, area, total):
    total1 = total2 = total3 = total4 = False

    if area[y][x] == 9:
        return total
    elif area[y][x] == 0:
        return False

    # Visited
    area[x][y] = -1

    print x, y

    if x < len(area[0]) - 2:
        total1 = recursion(x + 1, y, area, total + 1)
    if y < len(area) - 2:
        total2 = recursion(x, y + 1, area, total + 1)
    if y > 0:
        total3 = recursion(x, y - 1, area, total + 1)
    if x > 0:
        total4 = recursion(x - 1, y, area, total + 1)

    listMin = []

    if total1:
        listMin.append(total1)
    if total2:
        listMin.append(total2)
    if total3:
        listMin.append(total3)
    if total4:
        listMin.append(total4)

    print listMin
    return min(listMin) if len(listMin) else 0


def minimumDistance(numRows, numColumns, area):
    q = collections.deque()
    q.append((0, 0, 0))

    while q:
        e = q.popleft()
        x, y, total = e[1], e[0], e[2]

        if area[x][y] == 9:
            return total
        elif area[x][y] == -1:
            continue

        area[x][y] = -1

        if y < len(area[0]) - 2 and area[x][y + 1]:
            q.append((x, y + 1, total + 1))
        if x < len(area) - 2 and area[x + 1][y]:
            q.append((x, y + 1, total + 1))
        if y > 0:
            q.append((x, y - 1, total + 1))
        if x > 0:
            q.append((x - 1, y, total + 1))


print minimumDistance(5, 4, [[1, 1, 1, 1], [0, 1, 1,1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]])