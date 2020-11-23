nm = input().split(" ")
n=int(nm[0])
m=int(nm[1])
i=0
ns=1
s=".|."
dash = "-"
x= int((m-3)/2)
middle = int((m-7)/2)
count =(n-1)/2
while(i<count):
    print(dash*x + s*ns + dash*x)
    i=i+1
    x=x-3
    ns+=2

print(dash*middle + "WELCOME" + dash*middle )

j=count
nsr= n-2
xr=3
while(j>0):
    print(dash*xr + s*nsr + dash*xr)
    nsr -= 2
    xr +=3
    j=j-1
