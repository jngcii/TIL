from collections import deque

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
b = [[] for _ in range(n+1)]

ind = [0]*(n+1)
ind2 = [0]*(n+1)

d = [0]*(n+1)
check = [False]*(n+1)

for _ in range(m):
    x, y, z = map(int ,input().split())

    a[x].append((y, z))
    b[y].append((x, z))

    ind[y] += 1
    ind2[x] += 1

st, ed = map(int, input().split())

q = deque()

for i in range(1, n+1):
    if not ind[i]:
        q.append(i)

while q:
    x = q.popleft()

    for y, cost in a[x]:
        if d[y]<d[x]+cost:
            d[y] = d[x]+cost
        
        ind[y] -= 1
        if not ind[y]:
            q.append(y)

print(d[ed])

res = 0
ind = ind2
check[ed] = True

for i in range(1, n+1):
    if not ind[i]:
        q.append(i)

while q:
    x = q.popleft()

    for y, cost in b[x]:
        if check[x] and d[x]-d[y] == cost:
            res += 1
            check[y] = True
        ind[y] -= 1
        if not ind[y]:
            q.append(y)

print(res)