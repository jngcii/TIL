import heapq as hq

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((z, y))
    a[y].append((z, x))

check = [False]*(n+1)

check[1] = True

q = []

res = 0

for z, y in a[1]:
    hq.heappush(q, (z, y))

while q:
    cost, x = hq.heappop(q)
    if check[x]: continue
    check[x] = True
    res += cost

    for z, y in a[x]:
        hq.heappush(q, (z, y))

print(res)