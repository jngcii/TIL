from collections import deque
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def simulate(a, k, x, y):
    if a[x][y] == '.':
        return (False, False, x, y)
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return (moved, False, x, y)
        if a[nx][ny] == '#':
            return (moved, False, x, y)
        elif a[nx][ny] in 'RB':
            return (moved, False, x, y)
        elif a[nx][ny] == '.':
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x,y = nx,ny
            moved = True
        elif a[nx][ny] == 'O':
            a[x][y] = '.'
            moved = True
            return (moved, True, x, y)

def go(b, rx, ry, bx, by, direction):
    a = copy.deepcopy(b)
    a[rx][ry] = 'R'
    a[bx][by] = 'B'
    hole1 = False
    hole2 = False
    while True:
        rmoved, rhole, rx, ry = simulate(a, direction, rx, ry)
        bmoved, bhole, bx, by = simulate(a, direction, bx, by)
        if not rmoved and not bmoved:
            break
        if rhole:
            hole1 = True
        if bhole:
            hole2 = True
    return (hole1, hole2, rx, ry, bx, by)

n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
d = [[[[-1]*m for k in range(n)] for j in range(m)] for i in range(n)]
ans = -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':
            hx,hy = i,j
        elif a[i][j] == 'R':
            rx,ry = i,j
            a[i][j] = '.'
        elif a[i][j] == 'B':
            bx,by = i,j
            a[i][j] = '.'
q.append((rx,ry,bx,by))
d[rx][ry][bx][by] = 0
found = False
while q:
    rx,ry,bx,by = q.popleft()
    for k in range(4):
        hole1,hole2,nrx,nry,nbx,nby = go(a,rx,ry,bx,by,k)
        if hole2:
            continue
        if hole1:
            found = True
            ans = d[rx][ry][bx][by] + 1
            break
        if d[nrx][nry][nbx][nby] != -1:
            continue
        q.append((nrx,nry,nbx,nby))
        d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1
    if found:
        break
print(ans)
