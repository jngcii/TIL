def init(tree, where, start, end, idx):
    if idx >= len(where):
        return
    if start == end:
        where[idx] = [start, end]
        return
    else:
        mid = (start + end) // 2
        init(tree, where, start, mid, idx*2)
        init(tree, where, mid+1, end, idx*2+1)
        where[idx] = [start, end]
    
def go(x, y, tree, where, i):
    cx = where[i][0]
    cy = where[i][1]
    mid = (cx + cy) // 2
    if x == cx and y == cy:
        tree[i] += 1
        return
    if x <= mid and y <= mid:
        go(x, y, tree, where, i*2)
    elif x <= mid and y > mid:
        go(x, mid, tree, where, i*2)
        go(mid+1, y, tree, where, i*2+1)
    elif x > mid and y > mid:
        go(x, y, tree, where, i*2+1)

def find(x, where):
    i = 1
    while True:
        cx = where[i][0]
        cy = where[i][1]
        if cx == cy == x:
            return i
        mid = (cx + cy) // 2
        if cx <= x <= mid:
            i = i * 2
        else:
            i = i * 2 + 1


def solution(n, sprints):
    h = 1
    while 2**h < n:
        h += 1
    size = 2**(h+1)
    tree = [0]*size
    where = [[] for _ in range(size)]
    init(tree, where, 1, n, 1)

    a = [0]*(n+1)
    order = []
    for i in range(len(sprints)-1):
        x, y = sprints[i], sprints[i+1]
        if x > y: x, y = y, x
        order.append((x, y))
    
    for x, y in order:
        go(x, y, tree, where, 1)
    
    for i in range(1, n+1):
        idx = find(i, where)
        while idx != 1:
            a[i] += tree[idx]
            idx = idx // 2
        a[i] += tree[idx]

    res = 0
    idx = 0
    for i in range(1, n+1):
        if res < a[i]:
            res, idx = a[i], i
    
    return idx


if __name__ == '__main__':
    n = 9
    sprints = [9, 7, 3, 1]
    print(solution(n, sprints))
