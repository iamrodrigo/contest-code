a = input()

for i in range(a):
    b = raw_input()
    total = 0
    for c in range(0, len(b)):
        temp = 0
        if c % 2 != 0:
            temp = int(b[c]) * 2
            if temp >= 10:
                temp = (temp - 10) + 1
        else:
            temp = int(b[c])
        total += temp

    total = total % 10
    if total > 0:
        total = 10 - total

    print total        
