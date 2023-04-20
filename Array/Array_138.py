a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listprocess=[]
for i in range(len(listin),0,-1):
    listout=[]
    for j in listin:
        if listin.count(j) == i and j not in listout:
            listout.append(j)
    listout.sort(reverse=True)
    listprocess = listprocess + listout
print(*listprocess)
