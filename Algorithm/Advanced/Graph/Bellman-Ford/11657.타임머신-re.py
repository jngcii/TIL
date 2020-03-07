n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

inf = 1000000000
dist = [inf]*(n+1)
dist[1] = 0

time_stone = False

for i in range(1, n+1):
    
    for x, y, z in a:
        if dist[x]!=inf and dist[y] > dist[x] + z:
            dist[y] = dist[x] + z
            if i == n:
                time_stone = True

if time_stone:
    print(-1)
else:
    for i in range(2, len(dist)):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])