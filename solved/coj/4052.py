a = int(input())

for i in range(a):
  b = raw_input()
  bLength = len(b)//2
  x = 0
  string = ""
  
  for j in range(bLength):
    string += (b[x+1] * int(b[x]))
    x = x+2

  print(string)
