def go(i, j):
    if d[i][j] != -1:
        return d[i][j]

    d[i][j] = 0

    # 한쪽짜리가 1개 이상 있을경우에만, 한쪽을 반쪽으로 쪼갠 경우를 현재 경우에 포함 할 수 있다.
    if i > 0:
        d[i][j] += go(i-1, j+1)

    # 반쪽짜리가 1개 이상 있을 경우에만, 반쪽짜리가 한개 덜 있을 경우르 현재 경우에 포함 할 수 있다.
    if j > 0:
        d[i][j] += go(i, j-1)

    return d[i][j]

d = [[-1]*61 for _ in range(31)]

for i in range(61):
    d[0][i] = 1

go(30, 0)

a = []
p = int(input())

while p != 0:
    a.append(p)
    p = int(input())

for x in a:
    print(d[x][0])