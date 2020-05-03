from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
s = [[0]*(m+1) for _ in range(n+1)]
dist = [[-1]*m for _ in range(n)]

h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1
sc -= 1
fr -= 1
fc -= 1

dist[sr][sc] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i-1][j-1]

q = deque()

q.append((sr, sc))

while q:
    y, x = q.popleft()
    print(y, x)

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny and 0 <= nx and ny+h-1 < n and nx+w-1 < m:
            if s[ny+h][nx+w] - s[ny+h][nx] - s[ny][nx+w] + s[ny][nx] == 0:
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                
print(dist[fr][fc])