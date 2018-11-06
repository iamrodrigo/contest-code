import time

list1 = []

def division(n):
  for i in range(2, n):
    isPrimeNumber = True
    for j in range(2, int((i) ** 0.5) + 1):
      if i % j == 0:
        isPrimeNumber = False
        break
    if isPrimeNumber:
        list1.append(i)

a = input()

start_time = time.time()
division(a)
print("--- %s seconds ---" % (time.time() - start_time))