badges = []
_, students = input(), map(int, raw_input().split())

for i in xrange(0, len(students)):
    badgeAssigned = {}
    jump = i

    while True:
        if jump in badgeAssigned:
            badges.append(jump + 1)
            break
        else:
            badgeAssigned[jump] = 1
            jump = students[jump] - 1

print ' '.join(map(str, badges))

    

