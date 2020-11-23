def staircase(n):
    num =int(n)

    for i in range(1,n+1):
        vals = " "*(num-1)
        valt = "#"*i
        print(vals + valt)
        num= num-1
        i = i + 1

staircase(6)
