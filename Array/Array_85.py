a,b=map(int,input(":").split(" "))
list1=[int(num) for num in input().split(" ",a-1)]
count = list1.count(b)
if count > 0:
    print("yes",count)
else:
    print("no")
