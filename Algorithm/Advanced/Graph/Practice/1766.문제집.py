import heapq as hq

n, m = map(int, input().split())

a = [[] for _ in range(n+1)]

ind = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    ind[y] += 1

q = []
res = []

for i in range(1, n+1):
    if not ind[i]: hq.heappush(q, i)

while q:
    x = hq.heappop(q)
    res.append(x)

    for y in a[x]:
        ind[y] -= 1
        if not ind[y]: hq.heappush(q, y)

print(*res)