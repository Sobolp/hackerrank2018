def rotLeft(a, d):
    r = []
    for i in range(len(a)):
        x = d + i
        if (x >= len(a)):
            x = x - len(a)
        r.append(a[x])
    return r


l = [1,2,3,4,5]
res = rotLeft(l,4)
print(res)
