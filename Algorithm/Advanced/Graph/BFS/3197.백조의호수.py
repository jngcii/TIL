from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())

a = [list(input()) for _ in range(r)]

swan_check = [[False]*c for _ in range(r)]

y1 = x1 = y2 = x2 = -1

for i in range(r):
    for j in range(c):
        if a[i][j] == 'L':
            if y1 == -1:
                y1, x1 = i, j
            else:
                y2, x2 = i, j

swan_check[y1][x1] = True

water = deque()
nwater = deque()
swan = deque()
nswan = deque()

for i in range(r):
    for j in range(c):
        if a[i][j] != 'X':
            water.append((i, j))

swan.append((y1, x1))

res = -1

i = 0
while True:
    if swan_check[y2][x2]:
        res = i
        break
    while water:
        y, x = water.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < r and 0 <= nx < c): continue
            if a[ny][nx] == 'X':
                nwater.append((ny, nx))
                a[ny][nx] = '.'

    while swan:
        y, x = swan.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < r and 0 <= nx < c): continue
            if swan_check[ny][nx]: continue
            swan_check[ny][nx] = True
            if a[ny][nx] == 'X':
                nswan.append((ny, nx))
                continue
            swan.append((ny, nx))
    
    i += 1
    swan = nswan
    water = nwater
    nswan = deque()
    nwater = deque()

print(res)




