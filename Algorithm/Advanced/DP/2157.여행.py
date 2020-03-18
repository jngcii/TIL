n, m, k = map(int, input().split())
a = [[] for _ in range(n+1)]
d = [[-1]*(m+1) for _ in range(n+1)]
for _ in range(k):
    x, y, z = map(int, input().split())
    if x>=y:continue
    a[y].append((x, z))

d[1][0] = 0
d[1][1] = 0

for j in range(2, m+1):
    for i in range(1, n+1):
        for x, cost in a[i]:
            if d[x][j-1] == -1: continue
            d[i][j] = max(d[i][j], d[x][j-1] + cost)
        
print(max(d[n]))
