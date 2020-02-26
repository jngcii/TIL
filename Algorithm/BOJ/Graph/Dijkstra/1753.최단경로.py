import heapq as hq

v, e = map(int, input().split())

inf = 10000000000

k = int(input())

a = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, z = map(int, input().split())
    a[x].append((y, z))

dist = [inf]*(v+1)
check = [False]*(v+1)

dist[k] = 0

q = []

hq.heappush(q, (dist[k], k))

# heapq는 
# 야 거기 정점까지 갔어
# 거기 정점까지 최소 얼마들어
# 다음에 이거 빼서 점검해 이느낌

while q:
    _, x = hq.heappop(q)

    if check[x]: continue
    check[x] = True

    for ai in a[x]:
        y, cost = ai[0], ai[1]

        if dist[y] > dist[x] + cost:
            dist[y] = dist[x] + cost
            hq.heappush(q, (dist[y], y))
            
    
for i in range(1, v+1):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])