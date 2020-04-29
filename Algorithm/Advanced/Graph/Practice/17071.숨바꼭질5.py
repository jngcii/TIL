### prac 1

# from collections import deque

# n, k = map(int, input().split())

# dist = [-1]*500001

# q = deque()
# q.append(n)
# dist[n] = 0

# t = 1

# res = -1

# if n == k:
#     res = 0

# while n != k:
#     k += t
#     if k > 500000: break
#     nq = deque()

#     while q:
#         x = q.popleft()

#         for y in [x+1, x-1, 2*x]:
#             if 0 <= y && y <= 500000:
#                 if dist[y] != t:
#                     nq.append(y)
#                     dist[y] = t
    
#     if dist[k] == t:
#         res = t
#         break
    
#     t += 1
#     q = nq

# print(res)





### prac 2

# from collections import deque

# n, k = map(int, input())

# dist = [-1] * 500001

# dist[n] = 0

# q = deque()

# res = -1

# if n == k:
#     res = 0

# q.append(n)


# t = 1
# while n != k:
#     k += t

#     nq = deque()

#     while q:
#         x = q.popleft()

#         for y in [x+1, x-1, x*2]:
#             if dist[y] != t:
#                 dist[y] = t
#                 nq.append(y)
    
#     if dist[k] == t:
#         res = t
#         break
    
#     t += 1
#     q = nq

# print(res)





### best prac 1

# from collections import deque

# n, k = map(int, input().split())

# dist = [[-1]*2 for _ in range(500001)]

# q = deque()

# q.append((n, 0))
# dist[n][0] = 0

# while q:
#     x, t = q.popleft()

#     for y in [x+1, x-1, x*2]:
#         if dist[y][1-t] == -1:
#             dist[y][1-t] = dist[x][t] + 1
#             q.append((y, 1-t))

# res = -1

# t = 0

# while True:
#     k += t
#     if k > 500000: break
#     if dist[k][t%2] <= t:
#         res = t
#         break
#     t += 1

# print(res)



### best prac 2

n, k = map(int, input().split())
dist = [[-1]*2 for _ in range(500001)]
dist[n][0] = 0
q = deque()
q.append((n, 0))
while q:
    x, r = q.popleft()
    for y in [x+1, x-1, x*2]:
        if 0 <= y <= 500000 and dist[y][1-r] == -1:
            dist[y][1-r] = dist[x][r] + 1
            q.append((y, 1-t))
res = -1
t = 0
while True:
    k += t
    if k > 500000: break
    if dist[k][t%2] <= t:
        res = t
        break
    t += 1

print(res)
