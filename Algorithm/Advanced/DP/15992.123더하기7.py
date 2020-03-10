d = [[0]*(1001) for _ in range(1001)]
d[0][0] = 1

for i in range(1, 1001):
    cn, tmp = divmod(i, 3)
    if tmp: cn += 1
    for j in range(cn, i+1):
        d[i][j] += d[i-1][j-1]
        if i-2 >= 0:
            d[i][j] += d[i-2][j-1]
        if i-3 >= 0:
            d[i][j] += d[i-3][j-1]

        d[i][j] %= 1000000009

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    print(d[n][m])
