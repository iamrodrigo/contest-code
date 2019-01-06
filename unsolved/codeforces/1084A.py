_, floors = input(), map(int, raw_input().split())

total = 0

for i, f in enumerate(floors):
    total += ((i) * 4) * f

print total