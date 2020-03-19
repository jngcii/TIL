def go(i, u, v):

    if d[i][u][v] is not None:
        return d[i][u][v]

    if i < u or i < v:
        return 0
    
    if i == 0 or u == 0 or v == 0:
        return 0

    d[i][u][v] = 0
    res = go(i-1, u-1, v-1) + up[u]*down[v]
    if u-1 >= 0 and i-1 >= v:
        res = max(res, go(i-1, u-1, v))
    if v-1 >= 0 and i-1 >= u:
        res = max(res, go(i-1, u, v-1))

    d[i][u][v] = res
    return res

n = int(input())

up = list(map(int, input().split()))
up = [0] + [i for i in up if i != 0]
down = list(map(int, input().split()))
down = [0] + [i for i in down if i != 0]

u_max = len(up) - 1
v_max = len(down) - 1

d = [[[None]*(v_max+1) for _ in range(u_max+1)] for _ in range(n+1)]

print(go(n, u_max, v_max))
