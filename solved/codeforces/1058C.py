a = input()
numbers = list(raw_input())

def luckyTicket(valueToSearch, array):
    if not len(array):
        return False

    total = 0
    for i, n in enumerate(array):
        total += int(n)
        if total < valueToSearch:
            continue
        elif total > valueToSearch:
            return False
        elif total == valueToSearch:
            while i+1 != len(array):
                if array[i+1] == '0':
                    i += 1
                else:
                    return luckyTicket(valueToSearch, array[i+1:])
            return True

sum = 0
for i, x in enumerate(numbers):
    sum += int(x)
    flag = luckyTicket(sum, numbers[i+1:])
    if flag:
        print "YES"
        exit()

print "NO"