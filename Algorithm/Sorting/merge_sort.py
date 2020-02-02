def merge_sort(a):

    n = len(a)

    if n <= 1:
        return

    mid = n//2

    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = i2 = ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            ia += 1
            i1 += 1

        else:
            a[i] = g2[i2]
            ia += 1
            i2 += 2

    while i1 < len(g1):
        a[ia] = g1[i1]
        ia += 1
        i1 += 1

    while i2 < len(g2):
        a[ia] = g2[i2]
        ia += 1
        i2 += 1


a = [2,6,8,3,7,5,4,1,9,10]
merge_sort(a)