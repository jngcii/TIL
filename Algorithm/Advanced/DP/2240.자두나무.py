def go(i, j):

    if i == 0 and j > 0:
        return -99999999
    if j < 0 or i < 0:
        return -99999999

    if d[i][j] != -1:
        return d[i][j]

    d[i][j] = 0

    if a[i] == j%2 + 1:
        d[i][j] = max(go(i-1, j-1) + 1, go(i-1, j) + 1)
    else:
        d[i][j] = max(go(i-1, j-1), go(i-1, j))

    return d[i][j]

n, m = map(int, input().split())

a = [0] + [int(input()) for _ in range(n)]

d = [[-1]*(m+1) for _ in range(n+1)]

d[1][0] = 1 if a[1] == 1 else 0
d[1][1] = 1 if a[1] == 2 else 0

res = 0
for i in range(0, m+1):
    res = max(res, go(n, i))

print(res)