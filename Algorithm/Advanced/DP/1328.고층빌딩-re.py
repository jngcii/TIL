N, L, R = map(int, input().split())

d = [[[0]*(R+1) for _ in range(L+1)] for _ in range(N+1)]

d[1][1][1] = 1

for i in range(2, N+1):
    for left in range(1, L+1):
        for right in range(1, R+1):
            d[i][left][right] += d[i-1][left][right-1]
            d[i][left][right] += d[i-1][left-1][right]
            d[i][left][right] += d[i-1][left][right]*(i-2)
            d[i][left][right] %= 1000000007

print(d[N][L][R])