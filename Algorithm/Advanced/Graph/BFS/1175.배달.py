# 틀렸음.. 다시해보기
# https://www.acmicpc.net/problem/1175
# https://www.acmicpc.net/source/share/16e9dc719503409ea94c7c8323d2547e

from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]

d = [[[[-1]*3 for _ in range(4)] for _ in range(m)] for _ in range(n)]

q = deque()

sy = sx = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            sy, sx = i, j

for i in range(4):
    d[sy][sx][i][0] = 0
    q.append((sy, sx, i, 0))

while q:
    py, px, pd, pz = q.popleft()

    if pz == 2:
        print(d[py][px][pd][2])
        exit()

    for i in range(4):
        if i != (pd+1)%4 and i!= (pd+3)%4:
            continue

        ny, nx = py+dy[i], px+dx[i]

        if 0<=ny<n and 0<=nx<m:
            nz = pz
            if a[ny][nx] == '#':
                continue
            if a[ny][nx] == 'C':
                nz += 1
            if nz>=3:
                continue
            if d[ny][nx][i][nz] == -1:
                d[ny][nx][i][nz] = d[py][px][pd][pz] + 1
                q.append((ny, nx, i, nz))

print(-1)