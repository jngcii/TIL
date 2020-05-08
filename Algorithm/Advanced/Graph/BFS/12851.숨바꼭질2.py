from collections import deque

n, k = map(int, input().split())

cnt = [-1]*100001

dist = [-1]*100001

cnt[n] = 1
dist[n] = 0

q = deque()

q.append(n)

while q:
    x = q.popleft()

    for y in [x-1, x+1, x*2]:
        if not (0 <= y <= 100000): continue

        if dist[y] == -1:
            dist[y] = dist[x] + 1
            cnt[y] = cnt[x]
            q.append(y)
        elif dist[y] == dist[x] + 1:
            cnt[y] += cnt[x]

print(dist[k])
print(cnt[k])