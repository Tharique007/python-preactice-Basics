a=int(input(":"))
list1=[int(sal) for sal in input().split(" ",a-1)]
list1.sort()
print(*list1)
