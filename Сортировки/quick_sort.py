def quick_sort(A, l=0, r=0):
    def partition(a, l , r):
        x = a[l]
        j = l
        for i in range(l+1, r):
            if a[i] <= x:
                j += 1
                a[j], a[i] = a[i], a[j]
        a[l], a[j] = a[j], a[l]
        return j

    r = r if r != 0 else len(A)
    if l >= r:
        return
    m = partition(A, l, r)
    quick_sort(A, l, m-1)
    quick_sort(A, m+1, r)

if __name__ == '__main__':
    pass