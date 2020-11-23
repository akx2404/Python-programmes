n=input("enter your number: ")
l=[]
for i in n:
    l.append(int(i))
print(l)
flag=0
j=len(l)
for a in range(j):
    if l[a] % (j-a)==0:
        print("{} is divisble by {}".format(l[a], j-a))
        flag+=1
    else:
        print("no")
        break
