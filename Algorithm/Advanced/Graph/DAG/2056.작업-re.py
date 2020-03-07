from collections import deque

n = int(input())

times = [0]*(n+1)
res = [0]*(n+1)

a = [[] for _ in range(n+1)]

ind = [0]*(n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))

    times[i] = tmp[0]
    j=2
    for _ in range(tmp[1]):
        a[tmp[j]].append(i)
        ind[i] += 1
        j += 1

q = deque()

for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i)
        res[i] = times[i]

while q:
    p = q.pop()

    for pi in a[p]:
        ind[pi] -= 1

        if res[pi] < res[p]+times[pi]:
            res[pi] = res[p]+times[pi]
        
        if not ind[pi]:
            q.append(pi)

ans = 0
for i in range(1, n+1):
    if ans < res[i]:
        ans = res[i]

print(ans)