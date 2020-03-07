def quick_sort(a, start, end):

    if end - start <= 0:
        return

    pivot = a[end-1]

    i = start

    for j in range(start, end):

        if a[j] <= pivot:

            a[i], a[j] = a[j], a[i]

            i += 1

    quick_sort(a, start, i-2)
    quick_sort(a, i, end)


a = [1,2,3,4,7,8,9,5]

quick_sort(a, 0, len(a))
