import sys
sys.setrecursionlimit(10**4)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def go(y, x):
    if y == n-1 and x == m-1:
        return 1
    if d[y][x] != -1:
        return d[y][x]

    d[y][x] = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if a[y][x] > a[ny][nx]:
                d[y][x] += go(ny, nx)

    return d[y][x]



n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1]*m for _ in range(n)]

res = go(0, 0)

print(res)