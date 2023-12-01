n = int(input())
s = str(input())
z = [0] * n

def zf(s):
    l = r = 0
    for i in range(1, n):
        if (i < r):
            z[i] = min(r - i, z[i - l])

        while (i + z[i] < n and s[i + z[i]] == s[z[i]]):
            z[i] += 1

        if i + z[i] > r:
            l = i
            r = i + z[i]

    return z


print(zf(s))