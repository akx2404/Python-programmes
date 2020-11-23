def longestSubarray(arr):
    count = 0
    max2=0
    l={}
    p=[]
    i=0
    while(i < len(arr)-1):
        a = arr[i]
        for j in range(len(arr)):
            if a == arr[j]:
                count += 1
                l.update({arr[j]:count})
                i+=1

    for (key, value) in l.items():
        print(str(key) + "::" + str(value))

    for k in l.values():
        p.append(k)

    p2=[p[0]]
    for z in range(1,(len(p))):
        p2.append(p[z]-p[z-1])

    print(p2)

    max =p2[0]
    for ele in range(len(p2)):
        if p2[ele] > max:
            max = p2[ele]
            print(max)
            for elem in range(len(p2)):
                if p2[elem] == max:
                    p2.remove(p2[elem])
                    max2 = p2[0]
                    for ele in range(len(p2)):
                        if p2[ele] > max2:
                            max2 = p2[ele]
                            print(max2)


longestSubarray([1,1,1,3,2,2,3,1,7,7,4,4,0,0,0,0,0,0])

