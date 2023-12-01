# Идея такая - бинпоиск по индексам строки.
# Если для i-го элемента префикс длины l совпадает с префиксом начала строки, то и l - 1 совпадает.
# Ищем максимальную l

def compute_z(string):
    n = len(string)
    z = [0] * n

    zbox_l, zbox_r, z[0] = 0, 0, 0
    for i in range(1, n):
        if i < zbox_r:              # i is within a zbox
            k = i - zbox_l
            if z[k] < zbox_r - i:
                z[i] = z[k]         # Full optimization
                continue
            zbox_l = i              # Partial optimization
        else:
            zbox_l = zbox_r = i     # Match from scratch
        while zbox_r < n and string[zbox_r - zbox_l] == string[zbox_r]:
            zbox_r += 1
        z[i] = zbox_r - zbox_l
    return z

s = str(input())
print(*compute_z(s))
