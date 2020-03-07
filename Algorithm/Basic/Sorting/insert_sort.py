def insert_sort(a):

    for i in range(1, len(a)):

        key = a[i]

        for j in range(i-1, -1, -1):

            if key < a[j]:

                a[j+1] = a[j]

                a[j] = key

    
a = [2,4,5,1,3]
insert_sort(a)