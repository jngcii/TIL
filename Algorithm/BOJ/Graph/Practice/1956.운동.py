v, e = map(int, input().split())

a = [[] for _ in range(v+1)]
inf = 100000000000
dist = [[inf]*(v+1) for _ in range(v+1)]


for _ in range(e):
    x, y, z = map(int, input().split())
    if dist[x][y]>z:
        dist[x][y] = z

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if dist[i][k] != inf and dist[k][j] != inf:
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]

res = inf

for i in range(1, v+1):
    if res>dist[i][i]:
        res = dist[i][i]

if res == inf:
    res = -1
print(res)