n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
d = [[0]*m for _ in range(n)]

for i in range(n):
    if a[i][0] == '1': d[i][0] = 1
for j in range(m):
    if a[0][j] == '1': d[0][j] = 1

for i in range(1, n):
    for j in range(1, m):
        if a[i][j] == '0': continue
        d[i][j] = min(d[i-1][j], d[i-1][j-1], d[i][j-1]) + 1

res = 0
for i in range(n):
    res = max(res, max(d[i]))

print(res**2)
