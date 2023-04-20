a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
count=0
for i in range(0,a):
    for j in range(i,a):
        count += 1
print(count)
