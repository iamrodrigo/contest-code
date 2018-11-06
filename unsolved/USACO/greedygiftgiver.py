"""
ID: noiarek1
LANG: PYTHON2
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

listOfNames = {}

a = int(fin.readline())
for n in xrange(a):
    listOfNames[fin.readline()[:-1]] = 0

givingMoney = fin.readline()
while givingMoney != '':
    money, between = map(int, fin.readline().split())

    if between == 0:
        givingMoney = fin.readline()
        continue

    totalGiven = money / between

    for _ in xrange(between):
        listOfNames[fin.readline()[:-1]] += totalGiven

    listOfNames[givingMoney[:-1]] += money % between

    givingMoney = fin.readline()[:-1]


for key, value in listOfNames.items():
    fout.write ("{} {}\n".format(key, value))

fout.close()