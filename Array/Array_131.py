a,b =map(int,input(":").split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
listout=[]
for i in listin:
    if listin.count(i) == b and (i not in listout):
        listout.append(i)
listout.sort()
if len(listout) > 0:
    print(*listout)
else:
    print(-1)

