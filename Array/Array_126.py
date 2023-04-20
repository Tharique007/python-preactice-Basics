a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listout=[]
for i in listin:
    if i <a:
        listout.append(i)
listout.sort(reverse=True)

if len(listout) > 0:
    print(*listout)
else:
    print(-1)