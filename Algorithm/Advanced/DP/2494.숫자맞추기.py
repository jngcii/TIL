# 오답

import sys
sys.setrecursionlimit(10**9)

def go(idx, turn):
    if idx >= n:
        return 0
    if d[idx][turn] != -1:
        return d[idx][turn]
    
    cur = (a[idx] + turn)%10

    cost_left = (b[idx] - cur + 10)%10
    left = cost_left + go(idx+1, (turn+cost_left)%10)

    cost_right = (cur - b[idx] + 10)%10
    right = cost_right + go(idx+1, turn)

    if left < right:
        d[idx][turn] = left 
    else:
        d[idx][turn] = right

    return d[idx][turn]


n = int(input())
a = [int(s) for s in input()]
b = [int(s) for s in input()]
d = [[-1]*10 for _ in range(n)]

res = go(0, 0)

print(res)