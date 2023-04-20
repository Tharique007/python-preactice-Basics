a,b=map(int,input().split(" "))
list1=[int(num) for num in input().split(" ",a)]
diff=1
for i in range(1,a):
    if abs(list1[i]-list1[i-1]) == 1:
        pass
    else:
        diff=abs(list1[i] - list1[i - 1])
        break
if diff==1 and list1.__contains__(b):
    print((list1.index(b)+1))
else:
    print(-1)