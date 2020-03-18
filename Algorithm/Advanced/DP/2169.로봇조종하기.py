# def go(i, j, k):
#     if d[i][j][k] != None:
#         return d[i][j][k]

#     if k == 0:
#         if i == 0: return 0
#         for x in range(3):
#             d[i-1][j][x] = go(i-1, j, x)
#         d[i][j][k] = max(d[i-1][j])
#     elif k == 1:
#         if j == 0: return 0
#         for x in range(3):
#             d[i][j-1][x] = go(i, j-1, x)
#         d[i][j][k] = max(d[i][j-1])
#     else:
#         if j == m-1: return 0
#         for x in range(3):
#             d[i][j+1][x] = go(i, j+1, x)
#         d[i][j][k] = max(d[i][j+1])
    
#     return d[i][j][k]


# n, m = map(int, input().split())

# a = [list(map(int, input().split())) for _ in range(n)]
# d = [[[None for _ in range(3)] for _ in range(m)] for _ in range(n)]

# for i in range(3):
#     d[0][0][i] = a[0][0]

# for i in range(1, m):
#     d[0][i][1] = d[0][i-1][1] + a[0][i]

# res = max(go(n-1, m-1, 0), go(n-1, m-1, 1))
# print(res)


n, m = map(int, input().split())
inf = 100000000000000
a = [[] for _ in range(n+1)]
d = [[[-inf]*3 for _ in range(m+2)] for _ in range(n+1)]

for i in range(1, n+1):
    a[i] = [0] + list(map(int, input().split()))

d[1][1][1] = a[1][1]

for j in range(2, m+1):
    d[1][j][1] = d[1][j-1][1] + a[1][j]

for i in range(2, n+1):
    for j in range(1, m+1):
        d[i][j][0] = max(d[i-1][j]) + a[i][j]
        d[i][j][1] = max(d[i][j-1][0], d[i][j-1][1]) + a[i][j]
    for j in range(m, 0, -1):
        d[i][j][2] = max(d[i][j+1][0], d[i][j+1][2]) + a[i][j]

print(max(d[n][m]))