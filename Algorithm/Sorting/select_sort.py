def select_sort(a):

    for i in range(0, len(a)-1):

        for j in range(i+1, len(a)):

            if a[i] > a[j]:

                a[i], a[j] = a[j], a[i]


a = [5,7,1,3,4,8,2]
print(a)
select_sort(a)
print(a)