a,b,c,d = map(int, input().split())

if (b == d):
    chisl = a + c
    zn = d
    for nod in range(min(chisl, zn), 1, -1):
        if (chisl % nod == 0 and zn % nod == 0):
            chisl = chisl // nod
            zn = zn // nod
    print(chisl, zn)

else:
    chisl = (a * d) + (c * b)
    zn = b * d
    for nod in range(min(chisl, zn), 1, -1):
        if (chisl % nod == 0 and zn % nod == 0):
            chisl = chisl // nod
            zn = zn // nod
    print(chisl, zn)