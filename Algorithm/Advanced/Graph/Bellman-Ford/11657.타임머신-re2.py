n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

inf = 1000000000000
dist = [inf]*(n+1)

dist[1] = 0

nc = False

for k in range(1, n+1):

    for x, y, cost in a:
        if dist[x] != inf and dist[y]>dist[x] + cost:
            dist[y] = dist[x] + cost
            if k == n:
                nc = True

if nc:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])
