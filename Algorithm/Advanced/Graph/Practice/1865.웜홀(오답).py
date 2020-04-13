# 오답

t = int(input())

res = []

for _ in range(t):
    n, m, w = map(int, input().split())
    inf = 10000000000
    a = []

    for _ in range(m):
        x, y, z = map(int, input().split())
        a.append([x, y, z])

    for _ in range(w):
        x, y, z = map(int, input().split())
        a.append([x, y, -z])

    result = False
    for i in range(1, n+1):
            
        ok = False

        dist = [inf]*(n+1)
        dist[i] = 0

        for k in range(n*2-1):
            for x, y, cost in a:
                if dist[x] == inf: continue
                if dist[y] > dist[x] + cost:
                    dist[y] = dist[x] + cost
                    if k >= n-1:
                        ok = True
                        break
        if ok:
            result = True
            break
    if result:
        res.append('YES')
    else:
        res.append('NO')

for r in res:
    print(r)