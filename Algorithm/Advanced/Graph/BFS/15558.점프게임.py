from collections import deque
n,k = map(int,input().split())
a = [input() for _ in range(2)]
dirs = [(0,1),(0,-1),(1,k)]
dist = [[-1]*n for _ in range(2)]
q = deque()
q.append((0,0))
dist[0][0] = 0
ok = False
while q:
    x,y = q.popleft()
    for dx,dy in dirs:
        nx,ny = (x+dx)%2,y+dy
        if ny >= n:
            ok = True
            break
        if ny < 0:
            continue
        if dist[nx][ny] != -1:
            continue
        if a[nx][ny] == '0':
            continue
        if ny < dist[x][y] + 1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
    if ok:
        break
print(1 if ok else 0)
