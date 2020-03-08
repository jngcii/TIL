import heapq as hq

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
inf = 1000000000000
dist = [inf]*(n+1)
check = [False]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))

start, end = map(int, input().split())

dist[start] = 0
q = []
hq.heappush(q, (dist[start], start))

while q:
    _, x = hq.heappop(q)
    
    if check[x]: continue
    check[x] = True

    for y, cost in a[x]:
        if dist[y] > dist[x] + cost:
            dist[y] = dist[x] + cost
            hq.heappush(q, (dist[y], y))

print(dist[end])