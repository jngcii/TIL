from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    fr = [-1]*(n+1)
    how = [-1]*(n+1)
    dist = [-1]*(n+1)

    q = deque()
    q.append(1%n)
    how[1%n] = 1
    dist[1%n] = 0

    while q:
        now = q.popleft()
        for i in range(2):
            nxt = (now * 10 + i) % n
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                fr[nxt] = now
                how[nxt] = i
                q.append(nxt)

    if dist[0] == -1:
        print('BRAK')
    else:
        res = []
        i = 0
        while i != -1:
            res.append(str(how[i]))
            i = fr[i]
        res.reverse()
        print(''.join(res))