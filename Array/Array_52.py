A= int(input(":"))
list1=[int(n) for n in input().split(" ",A-1)]
list1.sort()
output1=-1
for i in range(0,A-1):
    if list1[i]>list1[0] and list1[i]<list1[i+1]:
        output1=list1[i]
        break
    elif i==(A-2) and list1[A-1]>list1[0]:
        output1 = list1[A-1]
        break
print(output1)

