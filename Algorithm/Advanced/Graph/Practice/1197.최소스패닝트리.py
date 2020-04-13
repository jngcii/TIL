import heapq as hq

v, e = map(int, input().split())

a = [[] for _ in range(v+1)]
check = [False]*(v+1)
res = 0
for _ in range(e):
    x, y, cost = map(int, input().split())
    a[x].append((cost, y))
    a[y].append((cost, x))

check[1] = True
q = []
for i in a[1]:
    hq.heappush(q, i)

while q:
    cost, x = hq.heappop(q)

    if check[x]: continue
    check[x] = True
    res += cost

    for i in a[x]:
        hq.heappush(q, i)

print(res)