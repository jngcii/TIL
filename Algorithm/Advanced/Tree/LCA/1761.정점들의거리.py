from collections import deque

n = int(input())

a = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, z = map(int , input().split())

    a[x].append((y, z))
    a[y].append((x, z))

depth = [0]*(n+1)
parent = [0]*(n+1)
check = [False]*(n+1)
dist = [0]*(n+1)

q = deque()

q.append(1)
check[1] = True

while q:
    x = q.popleft()

    for y, cost in a[x]:
        if check[y]: continue

        check[y] = True
        dist[y] = dist[x]+cost
        depth[y] = depth[x]+1
        parent[y] = x
        q.append(y)

m = int(input())
ans = []

for _ in range(m):
    x, y = map(int, input().split())

    res = dist[x] + dist[y]

    if depth[x]<depth[y]:
        x, y = y, x
    
    while depth[x]<depth[y]:
        x = parent[x]

    while x!=y:
        x = parent[x]
        y = parent[y]

    res -= (dist[x]*2)

    ans.append(res)

for i in ans:
    print(i)