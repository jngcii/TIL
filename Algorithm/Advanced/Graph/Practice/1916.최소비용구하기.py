import heapq as hq

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
inf = 100000000
dist = [inf]*(n+1)
for _ in range(m):
    x, y, cost = map(int, input().split())
    a[x].append((y, cost))
s, e = map(int, input().split())
dist[s] = 0
q = []
hq.heappush(q, (dist[s], s))
while q:
    _, x = hq.heappop(q)

    for y, cost in a[x]:
        if dist[y] > dist[x] + cost:
            dist[y] = dist[x] + cost
            hq.heappush(q, (dist[y], y))
    
print(dist[e])