a = input()
rolls = []

for i in range(a):
    rolls.append(input())

rolls.sort()
lastElement = len(rolls) - 1
firstElement = 0
total = 0

while lastElement > firstElement:
    discount = rolls[firstElement] / 2.0
    total += rolls[lastElement] + discount
    lastElement -= 1
    firstElement += 1

if firstElement == lastElement:
    total = total + rolls[lastElement]

print "%.2f" % total