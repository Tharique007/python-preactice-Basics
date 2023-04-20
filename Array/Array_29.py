a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
list2=[int(num) for num in input().split(" ",a-1)]
list3=list1.copy()
sum=0
for i in list2:
    list3.append(i)
list3.sort()
#print(list3)
length = len(list3)
middle=0

if length%2 == 0:
    middle = int((length/2)-1)
    sum=list3[middle]+list3[(middle+1)]
elif (length%2) != 0:
    middle = int(length/2)
    sum = list3[middle]

print(sum)