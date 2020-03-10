N, L, R = map(int, input().split())

d = [[[0 for _ in range(R+1)] for _ in range(L+1)] for _ in range(N+1)]

d[1][1][1] = 1

for n in range(1, N):
    for i in range(1, L+1):
        for j in range(1, R+1):
            if i+1 <= L:
                d[n+1][i+1][j] += d[n][i][j]
                d[n+1][i+1][j] %= 1000000007
            if j+1 <= R:
                d[n+1][i][j+1] += d[n][i][j]
                d[n+1][i][j+1] %= 1000000007
            d[n+1][i][j] += (n-1)*d[n][i][j]
            d[n+1][i][j] %= 1000000007

print(d[N][L][R])