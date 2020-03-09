# Top down

# import sys
# sys.setrecursionlimit(10**4)

# def go(y, x):
#     if d[y][x] != -1:
#         return d[y][x]

#     d[y][x] = 0

#     d1 = go(y-1, x) + 1
#     d2 = go(y-1, x-1) + 1
#     d3 = go(y, x-1) + 1
#     if a[y][x] == '1':
#         d[y][x] = min(d1, d2, d3)

#     return d[y][x]

# n, m = map(int, input().split())

# a = [list(input()) for _ in range(n)]
# d = [[-1]*m for _ in range(n)]

# for i in range(n):
#     if a[i][0] == '1':
#         d[i][0] = 1
#     else:
#         d[i][0] = 0
# for j in range(m):
#     if a[0][j] == '1':
#         d[0][j] = 1
#     else:
#         d[0][j] = 0

# go(n-1, m-1)
# res = 0
# for i in range(n):
#     res = max(res, max(d[i]))

# print(res**2)


# Bottom up

n, m = map(int, input().split())

a = [['0']*(m+1)] + [(['0'] + list(input())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
res = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == '0': continue
        d[i][j] = min(d[i-1][j], d[i-1][j-1], d[i][j-1]) + 1
        if res < d[i][j]: res = d[i][j]
print(res**2)