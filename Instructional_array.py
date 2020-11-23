n = int(input())
l=[]
for i in range(n):
    e = input().split(" ")
    if e[0] == 'append':
        l.append(int(e(1)))
    elif e[0] == 'remove':
        l.remove(int(e(1)))
    elif e[0]== 'insert':
        l.insert(int(e(1)), int(e(2)))
    elif e[0]== 'print':
        print(l)
    elif e[0]== 'pop':
        l.pop()
    elif e[0]== 'reverse':
        l.reverse()