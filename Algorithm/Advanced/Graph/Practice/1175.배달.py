from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]

d = [[[[-1]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]

q = deque()

y1 = x1 = y2 = x2 = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if y1 == -1:
                y1 = i
                x1 = j
            else:
                y2 = i
                x2 = j
        elif a[i][j] == 'S':
            for k in range(4):
                d[i][j][0][k] = 0
                q.append((i, j, 0, k))

res = -1
while q:
    y, x, c, k = q.popleft()

    if c == 3:
        res = d[y][x][c][k]
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if not (0 <= ny < n and 0 <= nx < m): continue
        if i == k: continue
        if a[ny][nx] == '#': continue

        if ny == y1 and nx == x1:
            if c == 1: continue
            if c == 2:
                d[ny][nx][3][i] = d[y][x][c][k] + 1
                q.append((ny, nx, 3, i))
                break
            if d[ny][nx][1][i] == -1 or d[ny][nx][1][i] > d[y][x][0][k] + 1:
                d[ny][nx][1][i] = d[y][x][c][k] + 1
                q.append((ny, nx, 1, i))

        elif ny == y2 and nx == x2:
            if c == 2: continue
            if c == 1:
                d[ny][nx][3][i] = d[y][x][c][k] + 1
                q.append((ny, nx, 3, i))
                break
            if d[ny][nx][2][i] == -1 or d[ny][nx][2][i] > d[y][x][c][k] + 1:
                d[ny][nx][2][i] = d[y][x][c][k] + 1
                q.append((ny, nx, 2, i))

        else:
            if d[ny][nx][c][i] > d[y][x][c][k] + 1 or d[ny][nx][c][i] == -1:
                d[ny][nx][c][i] = d[y][x][c][k] + 1
                q.append((ny, nx, c, i))


print(res)