import time

list2 = []

def eratosthenes(n):
  list3 = [1] * n
  list3[0] = 0
  list3[1] = 0

  for i in range(2, int(n ** 0.5) + 1):
    if list3[i] == 0:
        continue

    for j in range(i * 2, len(list3), i):
        list3[j] = 0


  for i in range(len(list3)):
      if list3[i] == 1:
          list2.append(i)

start_time = time.time()
eratosthenes(1000000010)
print("--- %s seconds ---" % (time.time() - start_time))