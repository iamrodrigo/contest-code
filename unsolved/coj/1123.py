uglyNumbers = [1]
primeNumbers = [2, 3, 5]

def descomposition(n):
  index = 0
  while n != 1 and index < len(primeNumbers):
    if n % primeNumbers[index] == 0:
        n = n / primeNumbers[index]
    else:
        index = index + 1
  return True if n == 1 else False


def getNthUglyNumber(a):
  if len(uglyNumbers) >= a:
    return uglyNumbers[a-1]
  else:
    i = uglyNumbers[-1] + 1
    while len(uglyNumbers) < a:
      if descomposition(i):
        uglyNumbers.append(i)
      i = i + 1

  return uglyNumbers[-1]      
    

a = input()
while a:
  uglyNumber = getNthUglyNumber(a)  
  print uglyNumber
  a = input()
