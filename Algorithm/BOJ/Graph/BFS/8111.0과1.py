from collections import deque

t = int(input())

for _ in range(1, t+1):
    n = int(input())

    fr = [-1]*(n+1)      # y 를 만들기 전의 숫자  fr[y] = x
    how = [-1]*(n+1)     # x 에서 y를 만들때 1을 썻는지 0을 썻는지
    dist = [-1]*(n+1)    # y 숫자의 길이

    q = deque()
    q.append(1%n)
    dist[1%n] = 0
    how[1%n] = 1

    while q:
        p = q.popleft()
        
        for i in range(2):
            nxt = (p*10+i)%n
            if dist[nxt] == -1:
                dist[nxt] = dist[p] + 1
                fr[nxt] = p
                how[nxt] = i
                q.append(nxt)

    if dist[0] == -1:
        print('BRAK')
    else:
        ans = ''
        i = 0
        while i != -1:
            ans = str(how[i]) + ans
            i = fr[i]
        
        print(ans)