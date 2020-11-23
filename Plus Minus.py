def plusMinus(arr):
    zero=0
    pos=0
    neg=0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] >0:
            pos += 1
        else:
            neg += 1

    rz= zero/len(arr)
    rp= pos/len(arr)
    rn= neg/len(arr)

    print("{:.6f} \n{:.6f} \n{:.6f}".format(rz,rp,rn))


(plusMinus([-4,3,-9,0,4,1]))