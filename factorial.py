i=0
fact=1

n=int(input("Enter no.---   "))
      

for i in range(1,n,1):
    fact=fact*i
print("factorial of "+str(n)+" = "+str(fact))
