a,b=map(int,input().split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
listprocess=[]
listout=[]
for i in listin:
    if i not in listprocess:
        listprocess.append(i)
for i in listprocess:
    if listin.count(i) < b:
        listout.append(i)
listout.sort()
print(*listout)