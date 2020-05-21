from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
a = [[0]*m for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == '.':
            a[i][j] = 0
        elif line[j] == '#':
            a[i][j] = -1
        else:
            a[i][j] = ord(line[j])-ord('0')

q = [deque() for _ in range(p+1)]
next_q = [deque() for _ in range(p+1)]

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q[a[i][j]].append((i,j))

while True:
    ok = False
    for who in range(1, p+1):
        d = [[0]*m for _ in range(n)]
        while q[who]:
            ok = True
            x,y = q[who].popleft()
            if d[x][y] == s[who]:
                next_q[who].append((x,y))
            if a[x][y] > 0 and a[x][y] != who:
                continue
            a[x][y] = who
            for k in range(4):
                nx,ny = x+dx[k],y+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        d[nx][ny] = d[x][y] + 1
                        if d[nx][ny] <= s[who]:
                            a[nx][ny] = who
                            q[who].append((nx,ny))
        q[who] = next_q[who]
        next_q[who] = deque()
    if not ok:
        break

ans = [0]*(p+1)
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            ans[a[i][j]] += 1
print(' '.join(map(str,ans[1:])))