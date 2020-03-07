import heapq as hq

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
check = [False]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())

    a[x].append((z, y))
    a[y].append((z, x))

q = []

check[1] = True
for ai in a[1]:
    hq.heappush(q, ai)

res = 0

while q:
    cost, x = hq.heappop(q)

    if check[x]: continue
    check[x] = True
    res += cost

    for cost, y in a[x]:
        if check[y]: continue
        hq.heappush(q, (cost, y))

print(res)