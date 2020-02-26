n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

dist = [1000000000]*(n+1)
dist[1] = 0 #시작하는 곳까지는 0이다.

negative_cycle = False #음수싸이클인가?!

# n번 반복하는 이유는 음수 싸이클을 찾기 위해서이다.
for i in range(1, n+1):

    for e in a:
        x, y, z = e[0], e[1], e[2]

        if dist[x] != 1000000000 and dist[y]>dist[x]+z:
            dist[y] = dist[x]+z
            # n-1번 반복하면 무조건 최단 경로로 되어 있어야 하고, 
            # n번째 검사했을때  위 조건이 성립한다는 것은 최단경로가 바뀐다는 것인데,
            # n-1번째가 최단경로여야만 하므로 바뀌는 것은 말이 안된다.
            # 즉, n번째에서 최단경로가 바뀐다는 것은 음수 싸이클이라는 뜻이다!!!!
            if i==n:
                negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == 1000000000:
            dist[i] = -1
        print(dist[i])