x = int(input())

i, j = 1, 1
quad = 1
cube = 1
check = 1
res = 0
while check <= x:
    if quad == cube:
        i += 1
        quad = i**2
        check -= 1
    elif quad < cube:
        res = quad
        i += 1
        quad = i*i
    else:
        res = cube
        j += 1
        cube = j**3
    check += 1

print(res)


