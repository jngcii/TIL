# 오답

n = int(input())

a = [0]+[int(s) for s in list(input())]
b = [0]+[int(s) for s in list(input())]

d = [[0]*2 for _ in range(n+1)]

res = []

for i in range(1, n+1):
    tmp1 = d[i-1][0] + (b[i] + 10 - (d[i-1][0] + a[i])%10)%10
    tmp2 = d[i-1][1] + (b[i] + 10 - a[i])%10
    d[i][0] = min(tmp1, tmp2)

    tmp1 = d[i-1][0] + (a[i] + d[i-1][0] + 10 - b[i])%10
    tmp2 = d[i-1][1] + (a[i] + 10 - b[i])%10
    d[i][1] = min(tmp1, tmp2)

print(min(d[n]))
for i in range(1, n+1):
    if d[i][0] < d[i][1]:
        print(i, d[i][0]-min(d[i-1]))
    else:
        print(i, -(d[i][1]-min(d[i-1])))

# import sys
# sys.setrecursionlimit(10**9)

# def go(idx, turn):
#     if idx >= n:
#         return 0
#     if d[idx][turn] != -1:
#         return d[idx][turn]
    
#     cur = (a[idx] + turn)%10

#     cost_left = (b[idx] - cur + 10)%10
#     left = cost_left + go(idx+1, (turn+cost_left)%10)

#     cost_right = (cur - b[idx] + 10)%10
#     right = cost_right + go(idx+1, turn)

#     if left < right:
#         d[idx][turn] = left 
#     else:
#         d[idx][turn] = right

#     return d[idx][turn]


# n = int(input())
# a = [int(s) for s in input()]
# b = [int(s) for s in input()]
# d = [[-1]*10 for _ in range(n)]

# res = go(0, 0)

# print(res)