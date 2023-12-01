from itertools import permutations

n = int(input())
# letters = []

# for l in range(1, n+1):
#     letters.append(str(l))

for i in permutations('([)]', r = n):
    s = ''.join(i)
    print(s)

# def permutation(str):
#     if len(str) == 0:
#         return []
#
#     if len(str) == 1:
#         return str
#
#     l = []
#
#     for i in range(len(str)):
#         m = str[i]
#
#         ost_str = str[:i] + str[i+1:]
#
#         for j in permutation(ost_str):
#             l.append(m + j)
#
#     return l
#
# for i in permutation(letters):
#     print(i)


# for i in permutations(letters, r = n):
#     s = ''.join(i)
#     print(s)
