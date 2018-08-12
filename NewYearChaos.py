def minimumBribes(q):
    result = 0
    for i in range(len(q)):
        c = q[i] - (i + 1)
        if (c > 2):
            return 'Too chaotic'
        for ii in range(max(0, q[i] - 2),i):
            if (q[ii] > q[i]):
                result = result + 1
    return result

#l = [5,1,2,3,7,8,6,4]
l = [1,2,5,3,7,8,6,4]
#l = [2,5,1,3,4]
#l = [2,1,5,4,3]

result = minimumBribes(l)
print(result)

#1,2,5,3,7,8,6,4
#1,2,3,4,5,6,7,8
#1,2,3,5,4,6,7,8
#1,2,3,5,6,4,7,8
#1,2,3,5,6,7,4,8
#1,2,3,5,7,6,4,8
#1,2,3,5,7,6,8,4
#1,2,3,5,7,8,6,4


#1,2,5,3,4,6,7,8
#1,2,5,3,4,7,6,8
#1,2,5,3