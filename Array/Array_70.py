a,b=map(int,input().split(" "))
list1=[int(num) for num in input().split(" ",a-1)]
list2=[int(nu) for nu in input().split(" ",b-1)]
list3 = list1+list2
list3.sort()
print(*list3)
