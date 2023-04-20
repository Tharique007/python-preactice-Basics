a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
list2=[int(m) for m in input().split(" ",a-1)]
sum1=sum(list1)
sum2=sum(list2)
result= False

for i in range(0,a):
    sum1= sum1-list1[i]+list2[i]
    sum2=sum2-list2[i]+list1[i]
    if sum1 == sum2:
        result = True
        #print(i)
        break
    else:
        sum1 = sum1 + list1[i] - list2[i]
        sum2 = sum2 + list2[i] - list1[i]
if result:
    print("yes")
else:
    print("no")

