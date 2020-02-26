t = int(input())

for tc in range(1, t+1):
    n, m, w = map(int, input().split())

    mxm = 100000000

    a = []

    for _ in range(m):
        s, e, c = map(int, input().split())
        a.append((s, e, c))
        a.append((e, s, c))

    for _ in range(w):
        s, e, c = map(int, input().split())
        a.append((s, e, -c))

    d = [mxm]*(n+1)

    d[1] = 0

    negative_circle = False

    for i in range(1, n+1):

        for e in a:

            x, y, z = e[0], e[1], e[2]

            if d[x] != mxm and d[y]>d[x]+z:
                d[y] = d[x]+z

                if n==i:
                    negative_circle=True
    
    if negative_circle:
        print('YES')
    else:
        print('NO')