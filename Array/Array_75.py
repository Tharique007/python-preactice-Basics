a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
list2 = list1.copy()
k=0
swap=0
    
for i in range(0,a-1):
        if list2[i]>list2[i+1]:
            minimum = min(list2[i:a])
            #print(minimum)
            k = list2[i]
            #print(k)
            ind=list2.index(minimum)
            list2[i] = list2[ind]
            list2[ind] = k
            swap +=1
#print(*list2)
print(swap)