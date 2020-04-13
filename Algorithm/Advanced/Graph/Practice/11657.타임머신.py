n, m = map(int, input().split())
inf = 10000000000
a = [list(map(int ,input().split())) for _ in range(m)]

dist = [inf]*(n+1)
dist[1] = 0

ok = False

for k in range(n):
    for x, y, cost in a:
        if dist[x] == inf: continue
        if dist[y] > dist[x] + cost:
            dist[y] = dist[x] + cost
            if k == n-1:
                ok = True

if ok: print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == inf: print(-1)
        else: print(dist[i])
