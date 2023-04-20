a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
if len(listin)%2 == 0:
    b=int(len(listin)/2)
elif len(listin)%2 != 0:
    b = int((len(listin)-1) / 2)
lis1=listin[0:b]
lis2=listin[b:len(listin)]
lis1.sort()
lis2.sort(reverse=True)
listout=lis1+lis2
print(*listout)
