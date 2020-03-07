n = int(input())
m = int(input())

inf = 1000000000

a = [[]for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))

start, end = map(int, input().split())

dist = [inf]*(n+1)
dist[start] = 0

check = [False]*(n+1)

v = [-1]*(n+1)

# 모든 최단거리의 간선은 최대 n-1개이다.
for _ in range(n-1):
    mx = inf + 1
    x = -1

    for i in range(1, n+1):
        if not check[i] and mx>dist[i]:
            mx = dist[i]
            x = i
    
    check[x] = True

    for ai in a[x]:
        to, cost = ai[0], ai[1]
        if dist[to] > dist[x] + cost:
            dist[to] = dist[x] + cost
            v[to] = x

i = end
res = []
while i != -1:
    res.append(i)
    i = v[i]

res.reverse()

print(dist[end])
print(len(res))
print(*res)