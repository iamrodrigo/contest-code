a = input()
b = raw_input()

g = 0
maxSequence = 0
prevSequence = 0
actSequence = 0

for t in b:
    if t == 'G':
        g += 1
        actSequence += 1
    else:
        maxSequence = max(maxSequence, prevSequence + actSequence + 1)
        prevSequence = actSequence
        actSequence = 0

maxSequence = max(maxSequence, prevSequence + actSequence + 1)
print g if maxSequence > g else maxSequence
