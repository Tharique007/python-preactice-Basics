a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
list2=[]
output=[]
for i in list1:
    if i not in list2:
        list2.append(i)
list2.sort(reverse=True)
for i in list2:
    output.append(list1.index(i))
print(*output)