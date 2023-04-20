a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
ans=0

for i in range(1,len(list1)-1):
    if list1[i]<list1[i-1] and list1[i]<list1[i+1]:
        ans += (min(list1[i+1],list1[i-1])-list1[i])
print(ans)