# Top down
import sys
sys.setrecursionlimit(10**6)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def go(y, x):
    if d[y][x] != 0:
        return d[y][x]
    
    d[y][x] = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if a[y][x] < a[ny][nx]:
                d[y][x] = max(d[y][x], go(ny, nx)+1)
    
    return d[y][x]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n):
        tmp = go(i, j)
        res = max(res, tmp)

print(res)