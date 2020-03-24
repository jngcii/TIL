import heapq as hq

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, cost = map(int, input().split())
    a[x].append((y, cost))
    a[y].append((x, cost))

check = [False]*(n+1)
check[1] = True
q = []
for y, cost in a[1]:
    hq.heappush(q, (cost, y))

res = 0
while q:
    cost, x = hq.heappop(q)
    if check[x]: continue
    check[x] = True
    res += cost

    for y, z in a[x]:
        hq.heappush(q, (z, y))

print(res)