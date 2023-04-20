n=int(input(":"))
list1=[int(num) for num in input().split(" ",n-1)]
list2=[]
for i in range(1,n):
    list2.append(max(list1[i-1],list1[i]))
print(*list2)