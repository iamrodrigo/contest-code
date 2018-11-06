"""
ID: noiarek1
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
a = fin.readline()
b = fin.readline()

totalA = 1
totalB = 1

for c in a:
    if c.isalpha():
        totalA = (totalA * ((ord(c) - 64))) % 47

for c in b:
    if c.isalpha():
        totalB = (totalB * ((ord(c) - 64))) % 47

fout.write ('GO\n' if totalA == totalB  else 'STAY\n')
fout.close()