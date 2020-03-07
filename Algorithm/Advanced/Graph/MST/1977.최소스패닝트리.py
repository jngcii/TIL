def union(p, a, b):
    x = find(p, a)
    y = find(p, b)
    p[x] = y

def find(p, a):
    if a == p[a]:
        return a
    else:
        p[a] = find(p, p[a])
        return p[a]


v, e = map(int ,input().split())

a = [[] for _ in range(v+1)]

p = list(range(v+1))

q = []

for _ in range(e):
    x, y, cost = map(int, input().split())

    a[x].append(y)
    a[y].append(x)

    q.append((cost, y, x))
    
q.sort()

res = 0

for i in range(e):
    fr = q[i][1]
    to = q[i][2]

    x = find(p, fr)
    y = find(p, to)

    if x!=y:
        union(p, fr, to)
        res += q[i][0]

print(res)