from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

sol = '123456780'


a = [list(map(int, input().split())) for _ in range(3)]
check = {}

q = deque()

x = y = 0

start = ''

for i in range(3):
    for j in range(3):
        if a[i][j] == 0:
            y, x = i, j
        start += str(a[i][j])

check[start] = 0
q.append((start, y, x))

while q:
    cur, y, x = q.popleft()

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if 0<=ny<3 and 0<=nx<3:
            tmp = list(cur)
            tmp[3*y+x], tmp[3*ny+nx] = tmp[3*ny+nx], tmp[3*y+x]
            
            num = ''.join(tmp)

            if num in check:
                continue
            check[num] = check[cur] + 1
            q.append((num, ny, nx))

if sol in check:
    print(check[sol])
else:
    print(-1)