from collections import deque

n, m = map(int, input().split())

a = [[] for _ in range(n+1)]
check = [False]*(n+1)
ind = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    ind[y] += 1

res = []
q = deque()
for i in range(1, n+1):
    if not ind[i]:
        q.append(i)

while q:
    x = q.popleft()
    res.append(x)

    for y in a[x]:
        ind[y] -= 1
        if not ind[y]:
            q.append(y)

print(*res)