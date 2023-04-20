a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
count=0
for i in range(0,a-1):
    if list1[i+1] == list1.count(list1[i]):
        count +=1
print(count)