l = int(input())
array = list(map(int, input().split())) [:l]

def merge(arr1, arr2):
    i = j = 0
    sorted = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted.append(arr1[i])
            i += 1
        else:
            sorted.append(arr2[j])
            j += 1
    if i < len(arr1):
        sorted += arr1[i:]
    if j < len(arr2):
        sorted += arr2[j:]
    return sorted

def merge_sort(sp):
    if len(sp) == 1:
        return sp
    middle = len(sp) // 2
    left = merge_sort(sp[:middle])
    right = merge_sort(sp[middle:])
    return merge(left, right)

if l != 0:
    print(*merge_sort(array))