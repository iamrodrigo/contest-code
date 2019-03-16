a = input()
b = raw_input()
ternaryString = [0, 0, 0]


def replace_right(source, target, replacement, replacements=None):
    return replacement.join(source.rsplit(target, replacements))

def replace(first, second, third):
    expected = a / 3

    if ternaryString[first] < expected:
        z = max(0, ternaryString[second] - expected)
        x = max(0, ternaryString[third] - expected)

        if z > (expected - ternaryString[first]):
            z = z - (expected - ternaryString[first])
        if x > (expected - ternaryString[first]):
            x = x - (expected - ternaryString[first])

        ternaryString[first] += z
        ternaryString[second] -= z

        ternaryString[first] += x
        ternaryString[third] -= x

        return (z, x)
    else:
        return (0, 0)

for i in b:
    ternaryString[int(i)] += 1

if ternaryString[0] == ternaryString[1] == ternaryString[2]:
    print b
else:
    z, x = replace(2, 1, 0)
    b = replace_right(b, '1', '2', z)
    b = replace_right(b, '0', '2', x)

    #b = replace(1, 0, 2)

    z, x = replace(0, 1, 2)
    b.replace('1', '0', z)
    b.replace('2', '0', x)

    print b





