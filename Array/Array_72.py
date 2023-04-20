a=int(input())
list1=[int(num) for num in input().split(" ",a-1)]
list2=list1.copy()
list3=list1.copy()
list2.sort()
list3.sort(reverse=True)

if list1 == list2 or list1 == list3:
    print("yes")
else:
    print("no")