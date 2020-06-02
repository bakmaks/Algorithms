import random
def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r):
        if a[i] <= x:       # Возможно только '<'
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(A, l, r):
    # r = r if r != 0 else len(A)
    if l >= r:
        return
    m = partition(A, l, r)
    quick_sort(A, l, m-1)
    quick_sort(A, m+1, r)


# def quicksort(nums, fst, lst):
#     if fst >= lst: return
#
#     i, j = fst, lst
#     pivot = nums[random.randint(fst, lst)]
#
#     while i <= j:
#         while nums[i] < pivot: i += 1
#         while nums[j] > pivot: j -= 1
#         if i <= j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i, j = i + 1, j - 1
#     quicksort(nums, fst, j)
#     quicksort(nums, i, lst)

if __name__ == '__main__':
    y = [4,2,3]
    quick_sort(y, 0, len(y))
    print(y)
    # quicksort(y, 0, len(y))
    # print(y)