a=int(input(":"))
list_1=[int(num) for num in input().split(" ",a-1)]
sum=0
for i in list_1:
    sum = sum + i

if sum % 2 ==0 and sum % 3 == 0 and sum % 5 ==0:
    print(1)
else:
    print(0)