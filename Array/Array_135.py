a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
lisprocess=listin.copy()
lisprocess.sort()
listout=[]
for i in lisprocess:
    listout.append((listin.index(i)+1))
print(*listout)