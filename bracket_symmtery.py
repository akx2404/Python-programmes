"""
The Project loaded in the IDE contains a boilerplate code for a Python based
application. Your task is to implement the details of the problem as follows:

Given  a string, determine whether or not the symbols  have its  mirror image.
The solution is expected to be implemented in the are_valid() of class 
mirrorsymbols.py  function.

Example for valid scenario like (), {} or [], or even ({}) and [()]:

1. "(a + b + c)"

2. "{(a + b) + (b / c)}

3. "[{a} - {b} + {(a * b)}]"

4. "{[}]" or "{[}(])" or "{()[()]}"

5. "a(b+c)"

Example for invalid scenario:

1. "a + b + c("

2. "{(a + b + (b / c)}"

3. "[{a - {b} + {(a * b)}"

4. ([(2+4] - 5) * [a+c]]

"""
#global
c1=0
c2=0
o1=0
o2=0
s1=0
s2=0
countc=0
counto=0
counts=0
flag = 0


inp = input("Enter input- ")
l = list(inp)
for i in l:
    if i == " ":
        l.remove(i)
#print(l)



brack = []
for j in range(len(l)):
    if l[j] == '{' or l[j] == '}' or l[j] == '[' or l[j] == ']' or l[j] == '(' or l[j] == ')':
        brack.append(l[j])
#print(brack)




for a in range(len(brack)):
    if brack[a] == '{':
        c1 = c1 + a
        countc = countc + 1
    if brack[a] == '}':
        c2 = c2 + a
        countc = countc + 1
    if brack[a] == '(':
        o1 = o1 + a
        counto = counto + 1

    if brack[a] == ')':
        o2 = o2 + a
        counto = counto + 1

    if brack[a] == '[':
        s1 = s1 + a
        counts = counts + 1

    if brack[a] == ']':
        s2 = s2 + a
        counts = counts + 1



        
if (s1+s2+o1+o2+c1+c2)==0 :
    flag=0
elif (countc)%2!=0 or (counto)%2!=0 or (counts)%2!=0:
    flag=0
else:
    if (countc==0 or (c2-c1)%2!=0) and (counto==0 or(o2-o1)%2!=0) and (counts==0 or(s2-s1)%2!=0) or (c2+s2+o2-o1-s1-c1)%4==0 or (c2+s2+o2-o1-s1-c1)%2!=0:
        flag=1

    else:
        flag=0




if flag==0:
    print("Invalid")

else:
    print("Valid")



































