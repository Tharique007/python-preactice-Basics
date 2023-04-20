a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
l2=[]
for i in list1:
    if list1.count(i) == 1:
        l2.append(i)
if len(l2) >0:
    print(*l2)
else:
    print(-1)