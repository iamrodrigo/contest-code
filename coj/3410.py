a = input()

list = {}

for i in range(a):
    b, c = map(int, raw_input().split())
    if b not in list:
        list[b] = 0
    list[b] = list[b] + c

output = sorted(list.keys())

for o in output:
    print str(o[0]) + " " + str(o[1])

#list.