import heapq as hq

n = int(input())
m = int(input())

inf = 10000000000000
dist = [inf]*(n+1)
check = [False]*(n+1)
a = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))

start, end = map(int, input().split())
dist[start] = 0
f = [-1]*(n+1)
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
            f[y] = x

stk = [end]
while f[end] != -1:
    stk.append(f[end])
    end = f[end]

stk.reverse()
print(dist[stk[-1]])
print(len(stk))
print(*stk)