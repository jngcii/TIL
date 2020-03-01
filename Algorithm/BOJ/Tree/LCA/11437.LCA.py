from collections import deque

n = int(input())

a = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())

    a[x].append(y)
    a[y].append(x)

depth = [0]*(n+1)
check = [False]*(n+1)
parent = [0]*(n+1)

q = deque()

check[1]=True
q.append(1)

while q:
    x = q.popleft()
    for y in a[x]:
        if check[y]: continue

        depth[y] = depth[x] + 1;
        check[y] = True
        parent[y] = x
        q.append(y)

m = int(input())

res = []

for _ in range(m):
    x, y = map(int, input().split())
    if depth[x]<depth[y]:
        x, y = y, x
    while depth[x] != depth[y]:
        x = parent[x]
    while x != y:
        x = parent[x]
        y = parent[y]
    
    res.append(x)

for ri in res:
    print(ri)