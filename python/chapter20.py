lst = [414252,1512366,679,12612346134713,1234,657145347,4613,1461243641371357868246,542,758,25723,2,46,7,2,42,5745,724]
def bubble_sort(lst):
    i = -1
    x = 0
    flag = True
    while flag == True:
        for e in lst[:-1]:
            i = i + 1
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                x = x + 1
        if x == 0:
            flag = False
        i = -1
        x = 0
    print(lst)
bubble_sort(lst)