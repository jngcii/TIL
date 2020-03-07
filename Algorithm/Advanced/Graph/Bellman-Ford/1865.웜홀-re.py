tc = int(input())

res = []
for _ in range(tc):
    n, m, w = map(int, input().split())

    a = []

    for _ in range(m):
        x, y, z = map(int, input().split())
        a.append((x, y, z))

    for _ in range(w):
        x, y, z = map(int, input().split())
        a.append((x, y, -z))

    inf = 10000000000
    dist = [inf]*(n+1)
    dist[1] = 0

    result = 'NO'

    for i in range(1, n+1):

        for x, y, z in a:

            if dist[x] != inf and dist[y]>dist[x]+z:
                dist[y] = dist[x] + z
                if i == n:
                    result = 'YES'
    
    res.append(result)

for r in res:
    print(r)
