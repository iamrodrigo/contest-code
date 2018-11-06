values = raw_input()
numbers = []

try:
    while values:
        for n in values.split():
            numbers.append(int(n[::-1]))
        values = raw_input()
except EOFError:
    True

numbers.pop(0)
numbers.sort()

for i in numbers:
    print i



