n = int(input())

three = []
for i in range(n):
    count, start, end = map(int, input().split())
    three.append([count, start, end])

for i in three:
    if i[1] + i[2] <= i[0]:
        print("YES")
    else:
        print("NO")