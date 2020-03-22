d = [[0]*1001 for _ in range(1001)]

d[0][0] = d[1][1] = d[2][1] = d[3][1] = 1

for i in range(2, 1001):
    tmp = i//3 if not i%3 else i//3 + 1
    for j in range(tmp, i+1):
        tmp2 = d[i-1][j-1] + d[i-2][j-1] + d[i-3][j-1]
        d[i][j] = tmp2 % 1000000009

t = int(input())
a = [list(map(int, input().split())) for _ in range(t)]

for n, m in a:
    print(d[n][m])