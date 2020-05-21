from collections import deque

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

dy1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dx1 = [1, 2, 2, 1, -1, -2, -2, -1]
dy2 = [0, 0, 1, -1]
dx2 = [1, -1, 0, 0]
dy3 = [1, 1, -1, -1]
dx3 = [1, -1, 1, -1]

d = [[[[-1]*3 for _ in range(n*n)] for _ in range(n)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(n):
        a[i][j] -= 1
        if not a[i][j]:
            for k in range(3):
                d[i][j][0][k] = 0
                q.append((i, j, 0, k))

res = -1

while q:
    y, x, num, p = q.popleft()
    if num == n*n - 1:
        if res == -1 or res > d[y][x][num][p]:
            res = d[y][x][num][p]
    
    # 말 교체
    for i in range(3):
        if p == i: continue
        if d[y][x][num][i] == -1:
            d[y][x][num][i] = d[y][x][num][p] + 1
            q.append((y, x, num, i))

    # 말 이동
    if p == 0:
        for k in range(8):
            ny, nx = y + dy1[k], x + dx1[k]
            if 0 <= ny < n and 0 <= nx < n:
                nxt = num
                if a[ny][nx] == num + 1:
                    nxt = num + 1
                if d[ny][nx][nxt][p] == -1:
                    d[ny][nx][nxt][p] = d[y][x][num][p] + 1
                    q.append((ny, nx, nxt, p))
    elif p == 1:
        for k in range(4):
            l = 1
            while True:
                ny, nx = y + dy2[k]*l, x + dx2[k]*l
                if 0 <= ny < n and 0 <= nx < n:
                    nxt = num
                    if a[ny][nx] == num + 1:
                        nxt = num + 1
                    if d[ny][nx][nxt][p] == -1:
                        d[ny][nx][nxt][p] = d[y][x][num][p] + 1
                        q.append((ny, nx, nxt, p))
                else:
                    break
                l += 1
    elif p == 2:
        for k in range(4):
            l = 1
            while True:
                ny, nx = y + dy3[k]*l, x + dx3[k]*l
                if 0 <= ny < n and 0 <= nx < n:
                    nxt = num
                    if a[ny][nx] == num + 1:
                        nxt = num + 1
                    if d[ny][nx][nxt][p] == -1:
                        d[ny][nx][nxt][p] = d[y][x][num][p] + 1
                        q.append((ny, nx, nxt, p))
                else:
                    break
                l += 1

print(res)