n = int(input())
lvls = list(map(int, input().split()))

sum_ned = 0
S_ned = 0
left = []
right = []
otv = []
for i in range(n):
    S_ned = (i) * lvls[i]
    left.append(S_ned - sum_ned)
    sum_ned += lvls[i]

sum_ned = 0
S_ned = 0
for j in range(n-1, -1, -1):
    i = abs(n - 1 - j)
    S_ned = (i) * lvls[j]
    right.append(sum_ned - S_ned)
    sum_ned += lvls[j]

print(left)
print(right)

right = right[::-1]
for k in range(n):
    otv.append(left[k] + right[k])

print(*otv)

# prefs = [0]*len(lvls)
# otv = []
#
# prefs[0] = lvls[0]

#[0]*len(lvls)

# for i in range(len(lvls)):
#     for j in range(len(lvls)):
#         prefs[j] = abs(lvls[j] - lvls[i])
#     otv.append(sum(prefs))

# for i in range(n):
#     prefs[i] = (abs(prefs[i-1] - lvls[i]))
#
# print(prefs)