import heapq as hq

v, e = map(int, input().split())
k = int(input())
inf = 1000000000
dist = [inf]*(v+1)
dist[k] = 0
a = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, cost = map(int, input().split())
    a[x].append((cost, y))

q = []
hq.heappush(q, (dist[k], k))

while q:
    _, x = hq.heappop(q)

    for cost, y in a[x]:
            
        if dist[y] > dist[x] + cost:
            dist[y] = dist[x] + cost
            hq.heappush(q, (dist[y], y))
            
for i in range(1, v+1):
    if dist[i] == inf: print('INF')
    else: print(dist[i])