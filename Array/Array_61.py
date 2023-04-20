a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
list2=[]
output=0
for i in list1:
    if i not in list2:
        list2.append(i)
frequency=0
for j in list2:
    if list1.count(j) > frequency:
        frequency=list1.count(j)
        output=j
print(output)
