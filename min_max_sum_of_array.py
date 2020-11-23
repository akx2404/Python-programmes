def miniMaxSum(arr):
    sum =0
    a=0
    s=[]
    mx=0
    mn=0
    for i in range(5):
        sum += arr[i]

    while(a<5):
        sumf = sum - arr[a]
        s.append(sumf)
        a= a+1

    mx = s[0]
    for x in range(1,5):
        if s[x]> mx:
            mx=s[x]

    mn = s[0]
    for l in range(1,5):
        if s[l]<mn:
            mn=s[l]

    print(s)
    print("{} {}".format(mx,mn))

miniMaxSum([1,3,5,7,9])







