n = int(input())
m = int(input())

inf = 1000000000000

a = [[inf]*n for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    x-=1
    y-=1
    if a[x][y] == inf or a[x][y]>z:
        a[x][y] = z

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                a[i][j]=0
                continue
            a[i][j] = min(a[i][j], a[i][k]+a[k][j])
            
for i in range(n):
    for j in range(n):
        if a[i][j] == inf:
            a[i][j] = 0

for i in range(n):
    print(*a[i])