n, m = list(map(int, input().split()))
lens = list(map(int, input().split()))

print(n, m)
print(lens)

#binary_search
start = 0
end = m - 1
wasFoud = False
sum = 0
weights = []

while(not wasFoud and start < end):
    middle = (start + end) / 2
    if (sum + lens[middle] == n) or (sum + (lens[middle] * 2) == n):
        wasFound = True
        if sum + lens[middle] == n:
            sum = sum + lens[middle]
            weights.append(lens[middle])
        if sum + (lens[middle] * 2) == n:
            sum + (lens[middle] * 2)
            weights.append(lens[middle] * 2)
