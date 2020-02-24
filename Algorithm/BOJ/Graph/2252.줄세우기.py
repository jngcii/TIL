### DFS ###

def go(x, a, check):
    check[x] = True

    for xi in a[x]:
        if not check[xi]:
            go(xi, a, check)
    
    print(x)


n, m = map(int, input().split())

a = [[] for _ in range(n+1)]
check = [False]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    a[y].append(x)

for i in range(n):
    if not check[i]:
        go(i, a, check)






### BFS ###

from collections import deque

n, m = map(int, input().split())

a = [[] for _ in range(n+1)]
ind = [0]*(n+1)
check = [False]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    ind[y] += 1

q = deque()

for i in range(1,n+1):
    if not ind[i]:
        q.append(i)

while q:
    p = q.pop()
    print(p)

    for ai in a[p]:
        ind[ai] -= 1
        if ind[ai] == 0:
            q.append(ai)