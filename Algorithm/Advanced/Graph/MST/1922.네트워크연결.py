import heapq

n = int(input())

m = int(input())

a = [[] for _ in range(n+1)]
c = [False]*(n+1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    a[tmp[0]].append((tmp[2], tmp[1]))
    a[tmp[1]].append((tmp[2], tmp[0]))
    
res = 0

q = []

c[1] = True

for ai in a[1]:
    heapq.heappush(q, ai)

while q:
    cost, p = heapq.heappop(q)

    if c[p]:
        continue

    c[p] = True
    res += cost

    for ai in a[p]:

        heapq.heappush(q, ai)

print(res)