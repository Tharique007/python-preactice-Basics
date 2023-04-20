a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listout=[]
for i in range(0,len(listin)):
    sum = 0
    for j in range(i,-1,-1):
        sum +=listin[j]
    if sum%2 == 0:
        listout.append(sum)
    elif sum%2 != 0:
        listout.append(listin[i])
print(*listout)

