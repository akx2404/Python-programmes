def birthdayCakeCandles(ar):
    max=ar[0]
    count=0

    for i in range(1,len(ar)):
        if ar[i]>max:
            max= ar[i]


    for j in range(len(ar)):
        if ar[j]== max:
            count +=1

    print(count)

birthdayCakeCandles([4,1,2,3])