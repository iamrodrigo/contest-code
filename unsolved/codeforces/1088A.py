a = input()

if a == 1:
    print -1
elif a == 2 or a == 3:
    print a, a
else:
    print a - 1 if (a - 1) % 2 == 0 else a, 2