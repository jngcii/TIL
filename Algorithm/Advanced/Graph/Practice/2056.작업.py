from collections import deque

n = int(input())

a = [[] for _ in range(n+1)]

ind = [0]*(n+1)
dist = [0]*(n+1)
res = [0]*(n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    ind[i] = tmp[1]
    dist[i] = tmp[0]
    for tmpi in tmp[2:]:
        a[tmpi].append(i)
        
q = deque()

for i in range(1, n+1):
    if not ind[i]:
        q.append(i)
        res[i] = dist[i]

while q:
    x = q.popleft()

    for y in a[x]:
        ind[y] -= 1

        if res[y] < res[x] + dist[y]:
            res[y] = res[x] + dist[y]

        if not ind[y]: q.append(y)

print(max(res))