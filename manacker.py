s = str(input())

z = [0] * len(s)
e = [0] * len(s)

def manacher_odd(s):
    l = 0
    r = -1
    for i in range(0, len(s)):
        if i > r:
            k = 1
        else:
            k = min(z[l + r - i], r - i + 1)
        while (i + k < len(s) and i - k >= 0 and s[i + k] == s[i - k]):
            k += 1
        z[i] = k
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1
    return z

def manacher_ev(s):
    l = 0
    r = -1
    for i in range(0, len(s)):
        if i > r:
            k = 0
        else:
            k = min(e[l + r - i + 1], r - i + 1)

        while (i + k < len(s) and i - k - 1 >= 0 and s[i + k] == s[i - k - 1]):
            k += 1

        e[i] = k

        if i + k - 1 > r:
            l = i - k
            r = i + k - 1
    return e

print(sum(manacher_odd(s)) + sum(manacher_ev(s)))