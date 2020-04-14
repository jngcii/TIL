def go(n, r, g, b):
    if n < 0 or r < 0 or g < 0 or b < 0: return 0

    if n == 0: return 1

    if d[n][r][g][b] != -1:
        return d[n][r][g][b]
    
    d[n][r][g][b] = 0
    if not n%3:
        tmp = n//3
        d[n][r][g][b] += go(n-1, r-tmp, g-tmp, b-tmp) * c[n][tmp] * c[n-tmp][tmp]

    if not n%2:
        tmp = n//2
        d[n][r][g][b] += go(n-1, r-tmp, g-tmp, b) * c[n][tmp]
        d[n][r][g][b] += go(n-1, r-tmp, g, b-tmp) * c[n][tmp]
        d[n][r][g][b] += go(n-1, r, g-tmp, b-tmp) * c[n][tmp]
        
    d[n][r][g][b] += go(n-1, r-n, g, b)
    d[n][r][g][b] += go(n-1 ,r ,g-n ,b)
    d[n][r][g][b] += go(n-1, r, g, b-n)

    return d[n][r][g][b]

        

N, R, G, B = map(int, input().split())

c = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]

d = [[[[-1]*(B+1) for _ in range(G+1)] for _ in range(R+1)] for _ in range(N+1)]

res = go(N, R, G, B)

print(res)