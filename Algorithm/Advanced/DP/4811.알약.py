def go(d, w, h):
    if d[w][h] != -1:
        return d[w][h]
    if w == 0:
        return 1
    if h == 0:
        d[w][h] = go(d, w-1, 1)
        return d[w][h]
    d[w][h] = go(d, w-1, h+1) + go(d, w, h-1)
    return d[w][h]


a = []

while not a or a[-1] != 0:
    m = int(input())
    a.append(m)

for n in a[:-1]:
    d = [[-1]*(n+1) for _ in range(n+1)]
    d[0][0] = 1

    # W가 i일때, H가 j일때의 경우의 수를 담는 2차원 배열
    print(go(d, n, 0))
