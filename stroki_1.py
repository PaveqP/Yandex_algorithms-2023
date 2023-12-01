s = str(input())
n = int(input())

data = []

for i in range(n):
    l, a, b = list(map(int, input().split()))
    data.append([l,a,b])

ns = len(s)
p = 10**9 + 7
x_ = 297
h = [0] * (ns + 1)
x = [0] * (ns + 1)
x[0] = 1
s = ' ' + s

for i in range(1, ns + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p

# print(ord('c'))
# print(h)
# print(x)

def isEqual(from1, from2, slen):
    # print((h[from2 + slen] - (h[from2] * x[slen])) % p)
    # print((h[from1 + slen] - (h[from1] * x[slen])) % p)
    return(
        ((h[from2 + slen] - (h[from2] * x[slen])) % p) == ((h[from1 + slen] - (h[from1] * x[slen])) % p)

    )
# print(isEqual(4, 0, 3))
for j in data:
    if isEqual(j[1], j[2], j[0]):
        print('yes')
    else:
        print('no')