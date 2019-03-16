import re

regex = raw_input()
pattern = re.compile('%s' % regex.replace("*", "."))

a = input()

list = []
count = 0

for i in range(a):
    plate = raw_input()
    if pattern.search(plate) is not None:
        list.append(plate)

print len(list)
for l in list:
    print l

