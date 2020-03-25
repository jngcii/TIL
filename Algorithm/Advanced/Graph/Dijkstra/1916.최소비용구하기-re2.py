import heapq as hq

n = int(input())
m = int(input())
inf = 100000000000
a = [[] for _ in range(n+1)]
d = [inf]*(n+1)

for _ in range(m):
    x, y, cost = map(int, input().split())
    a[x].append((cost, y))

start, end = map(int, input().split())

d[start] = 0

q = []

hq.heappush(q, (d[start], start))

while q:
    _, x = hq.heappop(q)

    for cost, y in a[x]:
        if d[y] > d[x] + cost:
            d[y] = d[x] + cost
            hq.heappush(q, (d[y], y))

print(d[end])