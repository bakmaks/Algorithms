def quick_sort(A, l=0, r=0):
    def partition(a, l , r):
        pass

    r = r if r != 0 else len(A)
    if l >= r:
        return
    m = partition(A, l, r)
    quick_sort(A, l, m+1)
    quick_sort(A, m, r)
