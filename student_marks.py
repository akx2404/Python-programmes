n = int(input())
inp=[]
p={}
marks=[]
c={}
marks1=[]
ans=[]

for i in range((2*n)):
    inp.append(input())

for j in range(0,len(inp),2):
    p[inp[j]]=float(inp[j+1])

marks = list(p.values())

for l in range(len(marks)):
    count = 0
    for l1 in range(len(marks)):
        if marks[l1]==marks[l]:
            count+=1
            c[marks[l]] = count

for k in range(len(marks)):
    if marks[k] not in marks1:
        marks1.append(marks[k])

marks1.sort()
secondsmall = marks1[1]

for name, p in p.items():
    if p == secondsmall:
        ans.append(name)

ans.sort()
for nam in range(len(ans)):
    print(ans[nam])
