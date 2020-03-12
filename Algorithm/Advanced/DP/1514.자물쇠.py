def go(i, j, k):
    if i == n: return 0
    if d[i][j][k] != -1: return d[i][j][k]
    origin = (a[i] + j)%10
    to = b[i]

    for three in range(10):
        for two in range(10):
            fr = (origin + two + three)%10
            one = (to - fr + 10)%10
            cost = turn[one] + turn[two] + turn[three]
            cost += go(i+1, (k+two+three)%10, three)
            if d[i][j][k] == -1 or d[i][j][k]>cost:
                d[i][j][k] = cost
    return d[i][j][k]

n = int(input())
a = [int(s) for s in input()]
b = [int(s) for s in input()]
turn = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1]
d = [[[-1 for _ in range(10)] for _ in range(10)] for _ in range(n)]

print(go(0,0,0))