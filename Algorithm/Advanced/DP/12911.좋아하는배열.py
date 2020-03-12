n, k = map(int, input().split())

d = [[0]*(k+1) for _ in range(n+1)]
total = [0]*11

divisors = [[] for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(i*2, k+1, i):
        divisors[j].append(i)

for i in range(1, k+1):
    d[1][i] = 1

total[1] = k

for i in range(2, n+1):
    for j in range(1, k+1):
        d[i][j] = total[i-1]
        for div in divisors[j]:
            d[i][j] -= d[i-1][div]
            d[i][j] %= 1000000007
            d[i][j] += 1000000007
            d[i][j] %= 1000000007
        total[i] += d[i][j]
        total[i] %= 1000000007

print(total[n])
