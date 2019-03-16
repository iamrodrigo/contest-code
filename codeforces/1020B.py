n = int(raw_input())
p = [int(x)-1 for x in raw_input().split()]

ans = [-1] * n
for i in range(n):
    if ans[i] == -1:
        visited = set()
        j = i
        while j not in visited:
            visited.add(j)
            j = p[j]
        k = i
        while k != j:
            ans[k] = j
            k = p[k]
        while ans[k] == -1:
            ans[k] = k
            k = p[k]

print ' '.join([str(x+1) for x in ans])

