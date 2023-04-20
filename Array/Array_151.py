a,b=map(int,input(":").split(" "))
listin=[int(n) for n in input("@:").split(" ",a-1)]
list1=listin[0:b]
list2=listin[b:len(listin)]
list1.sort()
list2.sort(reverse=True)
print(*(list1+list2))