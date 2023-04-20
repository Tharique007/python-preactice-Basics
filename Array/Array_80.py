a,b=map(int,input(":").split())
list1=[int(num) for num in input().split(" ",a-1)]
count=0
for i in list1:
    if i == b:
        count = 1
        break
if count == 1:
    print("Yes")
else:
    print("No")

