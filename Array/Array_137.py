a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listout=[]
for i in range(0,len(listin)):
    summ = sum(listin[i:len(listin)])
    listout.append(summ)
print(*listout)