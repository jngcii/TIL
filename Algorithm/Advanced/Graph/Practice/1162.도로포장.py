import heapq as hq

n, m, k = map(int, input().split())

a = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    a[x].append((y, z))
    a[y].append((x, z))

inf = 100000000000000000000

dist = [[inf]*(k+1) for _ in range(n+1)]
check = [[False]*(k+1) for _ in range(n+1)]

dist[1][0] = 0

q =[]
hq.heappush(q, (0, 1, 0))

while q:
    _, x, step = hq.heappop(q)
    if check[x][step]: continue
    check[x][step] = True

    for y, cost in a[x]:
        if step+1<=k and dist[y][step+1] > dist[x][step]:
            dist[y][step+1] = dist[x][step]
            hq.heappush(q, (dist[y][step+1], y, step+1))
        
        if dist[y][step]>dist[x][step]+cost:
            dist[y][step] = dist[x][step]+cost
            hq.heappush(q, (dist[y][step], y, step))

res = inf
for i in range(1, k+1):
    if check[n][i] and res>dist[n][i]:
        res = dist[n][i]

print(res)