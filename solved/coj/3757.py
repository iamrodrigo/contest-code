a = input()
primeNumbers = [2]

def calculateNextPrimeNumber(lastPrimeNumber):
  while True:
    lastPrimeNumber = lastPrimeNumber + 1
    isPrimeNumber = True
    for i in range(2, int((lastPrimeNumber) ** 0.5) + 1):
      if lastPrimeNumber % 2 == 0:
        isPrimeNumber = False
        break
    if isPrimeNumber:
      return lastPrimeNumber

          

for i in range(a):
  b = input()
  currentPrimeNumberIndex = 0
  primeFactors = {}
  while b != 1:
    
    if b % primeNumbers[currentPrimeNumberIndex] == 0:
      b = b / primeNumbers[currentPrimeNumberIndex]
      primeFactors[primeNumbers[currentPrimeNumberIndex]] = primeFactors[primeNumbers[currentPrimeNumberIndex]] + 1 if primeNumbers[currentPrimeNumberIndex] in primeFactors else 1
    else:
        if not currentPrimeNumberIndex + 1 < len(primeNumbers):
          primeNumbers.append(calculateNextPrimeNumber(primeNumbers[-1]))
        
        currentPrimeNumberIndex = currentPrimeNumberIndex + 1

  polynomial = []

  for key, value in primeFactors.items():
      tempArray = []
      for i in range(0, value + 1):
          tempArray.append(key ** i)

      polynomial.append(tempArray)

  while len(polynomial) > 1:
      listOne = polynomial.pop()
      listTwo = polynomial.pop()
      temp = []
      for i in listOne:
          for j in listTwo:
              temp.append(i * j)

      polynomial.append(temp)

  even = 0
  odd = 0

  for i in polynomial[0]:
      if i % 2 == 0:
          even = even + 1
      else:
          odd = odd + 1

  print "P: " + str(even) + " I: " + str(odd)



