a = input()

for i in range(a):
    lines, shifted = map(int, raw_input().split())
    shifted = shifted % 26
    for j in range(lines):
        line = raw_input()
        newLine = '';
        for x in range(0, len(line)):
            c = line[x]
            if c.isupper():
                asciiValue = ord(c)
                asciiValue = asciiValue + shifted
                if asciiValue > 90:
                    asciiValue = 64 + (asciiValue - 90)
                c = chr(asciiValue)

            print c,
        #print(newLine, end='')
