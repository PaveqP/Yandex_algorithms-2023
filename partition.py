import random
import sys

l = int(input())

sys.setrecursionlimit(2**30)

def quicksort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition(a, l, r)
    quicksort(a, l, m1 - 1)
    quicksort(a, m2 + 1, r)

def partition(arr, start, stop):
    x, j, t = arr[start], start, stop
    i = j
    while i <= t:
        if (arr[i] < x):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        elif (arr[i] > x):
            arr[i], arr[t] = arr[t], arr[i]
            t -= 1
            i -= 1
        i += 1
    return j, t

if l > 0:
    array = list(map(int, input().split()))
    quicksort(array, 0, l - 1)
    print(*array)