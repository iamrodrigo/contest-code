black = [[],[],[],[],[],[]]
white = [[],[],[],[],[],[]]

row = 9
column = 96

def valueOfPiece(c):
    return {
        'K': 0,
        'Q': 1,
        'R': 2,
        'B': 3,
        'N': 4,
        'P': 5,
    }.get(c)

for r in range(0, 17):
    string = raw_input()

    if r % 2 == 0:
        row = row - 1
        continue

    for i in xrange(2, len(string), 4):
        column += 1
        c = string[i]

        if not c.isalpha():
            continue

        t = c.upper()
        elementToInsert = "{}{}{}".format(t if t != 'P' else '', chr(column), row)

        if c.isupper():
            white[valueOfPiece(t)].append(elementToInsert)
        else:
            black[valueOfPiece(t)].append(elementToInsert)

    column = 96

whiteString = ""

for i in white:
    i.sort(key=lambda j: j[-1])
    whiteString += ",".join(i) + ","

blackString = ""

for i in black:
    blackString += ",".join(i) + ","

print "White: " + whiteString[0:-1]
print "Black: " + blackString[0:-1]