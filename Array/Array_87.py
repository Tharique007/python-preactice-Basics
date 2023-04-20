a,b=map(int,input(":").split(" "))
list1=[int(num) for num in input().split(" ",a-1)]
list2=[]
for i in range(0,(a-b)):
    list2.append(list1[i])
print(*list2)