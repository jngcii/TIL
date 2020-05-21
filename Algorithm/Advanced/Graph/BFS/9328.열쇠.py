from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['*.'+input()+'.*' for _ in range(n)]
    n += 4
    m += 4
    a = ['*'*m,'*'+'.'*(m-2)+'*'] + a + ['*'+'.'*(m-2)+'*','*'*m]
    key = set(input())
    ans = 0
    check = [[False]*m for _ in range(n)]
    q = deque()
    door = [deque() for _ in range(26)]
    q.append((1,1))
    check[1][1] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if check[nx][ny]:
                continue
            w = a[nx][ny]
            if w == '*':
                continue
            check[nx][ny] = True
            if w == '.':
                q.append((nx,ny))
            elif w == '$':
                q.append((nx,ny))
                ans += 1
            elif 'A' <= w <= 'Z':
                if w.lower() in key:
                    q.append((nx,ny))
                else:
                    door[ord(w)-ord('A')].append((nx,ny))
            elif 'a' <= w <= 'z':
                q.append((nx,ny))
                if not w in key:
                    key.add(w)
                    q.extend(door[ord(w)-ord('a')])
    print(ans)