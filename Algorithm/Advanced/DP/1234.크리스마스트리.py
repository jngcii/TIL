def go(n, r, g, b):
    if r<0 or g<0 or b<0:
        return 0
    
    if n == 0:
        return 1

    if d[n][r][g][b] != -1:
        return d[n][r][g][b]
    
    d[n][r][g][b] = 0
    d[n][r][g][b] += go(n-1, r-n, g, b)
    d[n][r][g][b] += go(n-1, r, g-n, b)
    d[n][r][g][b] += go(n-1, r, g, b-n)

    if not n%2:
        d[n][r][g][b] += go(n-1, r-n//2, g-n//2, b)*c[n][n//2]
        d[n][r][g][b] += go(n-1, r, g-n//2, b-n//2)*c[n][n//2]
        d[n][r][g][b] += go(n-1, r-n//2, g, b-n//2)*c[n][n//2]
    
    if not n%3:
        d[n][r][g][b] += go(n-1, r-n//3, g-n//3, b-n//3)*c[n][n//3]*c[n-n//3][n//3]
    
    return d[n][r][g][b]


N, R, G, B = map(int, input().split())

d = [[[[-1 for _ in range(B+1)] for _ in range(G+1)] for _ in range(R+1)] for _ in range(N+1)]

c = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]

print(go(N, R, G, B))