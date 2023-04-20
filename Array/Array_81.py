a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(*list2)