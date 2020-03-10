# def go(n):
#     if d[n] != -1:
#         return d[n]
    
#     res = 0
#     for i in range(1, n+1, 2):
#         res += (c[n-1][i-1]*go(i-1)*go(n-i))
#     d[n] = res
#     return res


# c = [[0]*21 for _ in range(21)]
# d = [-1]*21

# for i in range(1, 21):
#     c[i][0] = c[i][i] = 1
#     for j in range(1, i):
#         c[i][j] = c[i-1][j-1] + c[i-1][j]

# d[0] = d[1] = d[2] = 1

# t = int(input())

# for i in range(t):
#     n = int(input())
#     if n == 1: print(1)
#     else:
#         print(2*go(n))

d = [-1]*22
d[0] = d[1] = d[2] = 1
c = [[0]*22 for _ in range(22)]
for i in range(1, 21):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]

def go(n):
    if d[n]!=-1: return d[n]
    for k in range(1, n+1, 2):
        d[n] += (go(k-1)*go(n-k)*c[n-1][k-1])
    return d[n]

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1: print(1)
    else: print(go(n)*2)