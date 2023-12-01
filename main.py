N, M = map(int, input().split())
arr = list(map(int, input().split())) [:N]

pairs = []
for i in range(M):
    start, end = map(int, input().split())
    pairs.append([start, end])

for i in pairs:
    mn = min(arr [i[0] : i[1] + 1])
    mx = max(arr [i[0] : i[1] + 1])
    if (mn != mx):
        print(mx)
    else: print('NOT FOUND')
