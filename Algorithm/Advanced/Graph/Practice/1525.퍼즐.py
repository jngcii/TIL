from collections import deque

def go(a, i):
    res = []
    if i > 2:
        b = a[:i-3] + a[i] + a[i-2:i] + a[i-3]
        if i+1 != 9:
            b += a[i+1:]
        res.append(b)
    if i < 6:
        b = a[:i] + a[i+3] + a[i+1:i+3] + a[i]
        if i+4 != 9:
            b += a[i+4:]
        res.append(b)
    if i%3:
        b = a[:i-1] + a[i] + a[i-1]
        if i+1 != 9:
            b += a[i+1:]
        res.append(b)
    if i%3 != 2:
        b = a[:i] + a[i+1] + a[i]
        if i+2 != 9:
            b += a[i+2:]
        res.append(b)

    return res


solution = '123456780'

a = ''.join(list(input())) + ''.join(list(input())) + ''.join(list(input()))
a = a.replace(' ', '')

d = dict()

q = deque()

q.append((a, 0))
d[a] = 0

while q:
    x, c = q.popleft()
    idx = 0
    for i in range(9):
        if x[i] == '0':
            idx = i
            break
    for y in go(x, idx):
        if y in d: continue
        d[y] = c + 1
        q.append((y, c+1))

if solution in d:
    print(d[solution])
else:
    print(-1)

