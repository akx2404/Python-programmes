def simpleArraySum(ar):
    s = 0
    for i in range(len(ar)):
        s = s + ar[i]
    return s


print(simpleArraySum([1, 2, 3, 4, 5]))
