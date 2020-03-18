import sys
sys.setrecursionlimit(10**6)

def go(i, j):
    if j == 0:
        return 0
    if i <= 0:
        return -32768*101
    
    if d[i][j] is not None:
        return d[i][j]
    d[i][j] = 0
    res = go(i-1, j)
    for k in range(i, 0, -1):
        tmp = (go(k-2, j-1) + (s[i] - s[k-1]))
        res = max(res, tmp)
    d[i][j] = res
    return res


n, m = map(int, input().split())
a = [0]+[int(input()) for _ in range(n)]
d = [[None]*(m+1) for _ in range(n+1)]
s = [0]*(n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

print(go(n, m))