import heapq as hq

def go(start, n, a):
    inf = 10000000000
    d = [inf]*(n+1)
    check = [False]*(n+1)
    d[start] = 0
    q = []
    hq.heappush(q, (d[start], start))

    while q:
        _, x = hq.heappop(q)

        if check[x]: continue
        check[x] = True

        for y, cost in a[x]:
            if d[y]>d[x]+cost:
                d[y]=d[x]+cost
                hq.heappush(q, (d[y], y))
    
    return d



n, e = map(int, input().split())

a = [[] for _ in range(n+1)]

for _ in range(e):
    x, y, z = map(int, input().split())

    a[x].append((y, z))
    a[y].append((x, z))

v1, v2 = map(int, input().split())

d = go(1, n, a)
d1 = go(v1, n, a)
d2 = go(v2, n, a)

res1 = d[v1] + d1[v2] + d2[n]
res2 = d[v2] + d2[v1] + d1[n]

res1 = min(res1, res2)

if res1 >= 10000000000:
    res1 = -1

print(res1)

