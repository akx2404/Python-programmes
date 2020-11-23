def diagonalDifference(arr):
    sum1=0
    sum2=0
    a=0
    d1 =[]
    d2=[]
    diff=0
    b=0

    for i in range(len(arr)):
        while a <= len(arr[i]):
            element1=(arr[i][a])
            d1.append(element1)
            a = a + 1
            i = i + 1
            if i >= len(arr):
                break
            break
    for e in d1:
        sum1 += e

    for i in range(len(arr) - 1, -1, -1):
        while b <= len(arr[i]):
            element2 = (arr[i][b])
            d2.append(element2)
            b = b + 1
            i = i - 1
            if i < 0:
                break
            break

    for e2 in d2:
        sum2 += e2

    diff = abs(sum1-sum2)
    print(diff)


diagonalDifference([[11,2,4], [4,5,6], [10,8,-12]])