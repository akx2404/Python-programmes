n = int(input())
p={}
l=[]
sum =0
avg=0
for i in range(n):
    e = input().split(" ")
    l=[]
    for j in range(1,len(e)):
        p[e[0]] = l
        l.append(float(e[j]))

name=input()
l1=(p[name])
for k in range(len(l1)):
    sum += l1[k]
    avg = sum/ len(l1)

print("{:.2f}".format(avg))



