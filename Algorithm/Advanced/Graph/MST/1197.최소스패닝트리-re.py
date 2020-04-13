import heapq as hq

v, e = map(int, input().split())

a = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, z = map(int, input().split())
    a[x].append((z, y))
    a[y].append((z, x))

check = [False]*(v+1)

q = []

check[1]=True
for ai in a[1]:
    hq.heappush(q, ai)

res = 0

while q:
    cost, x = hq.heappop(q)
    if check[x]: continue
    check[x] = True

    res += cost

    for cost, y in a[x]:
        hq.heappush(q, (cost, y))

print(res)