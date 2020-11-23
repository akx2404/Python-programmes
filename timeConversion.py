def timeConversion(s):
    l=s.split(":",2)
    a= list(map(str,s))
    if a[8]=='P':
        hh = l[0]
        hi = int(hh)
        hif = hi +12
        if hif == 24:
            l[0] = '12'
        else:
            l[0] = hif

    elif a[8]=='A':
        hh = l[0]
        hi = int(hh)
        hif = hi + 0
        if hif == 12:
            l[0] = '00'
        else:
            l[0] = '0'+ str(hif)





    return "{}:{}:{}".format(l[0], l[1],l[2][0:2])

print(timeConversion("06:40:03AM"))