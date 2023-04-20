a,b=map(int,input().split(" "))
list1=[int(n) for n in input().split(" ",a-1)]
list2=[int(m) for m in input().split(" ",b-1)]
list3=[]
for i in list2:
    list1.append(i)
    list3.append(max(list1))
print(*list3)