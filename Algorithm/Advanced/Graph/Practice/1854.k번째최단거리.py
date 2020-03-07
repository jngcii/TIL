import heapq as hq

n, m, k = map(int, input().split())

a = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))

dist = [[] for _ in range(n+1)]

hq.heappush(dist[1], 0)

q = []

hq.heappush(q, (0, 1))

while q:
    cur, x = hq.heappop(q)

    for y, cost in a[x]:

        if len(dist[y]) < k or dist[y][-1]>cur+cost:
            if len(dist[y]) == k:
                hq.heappop(dist[y])
            hq.heappush(dist[y], (cur+cost))
            hq.heappush(q, (cur+cost, y))

for i in range(1, n+1):
    if len(dist[i]) != k:
        print(-1)
    else:
        print(dist[i][-1])