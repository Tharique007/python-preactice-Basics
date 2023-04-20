a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
list2= list1.copy()
list2.sort()
count=0
index=0
if list1 == list2:
    print(-1)
else:
    for i in range(0,a):
        if list1[i] != list2[i] and count < 2:
            k = list1[i]
            d = list1.index(list2[i])
            list1[i] = list2[i]
            list1[d]=k
            count +=1
            index = i
    if count > 1:
        print(-1)
    elif count ==1:
        print(index)
