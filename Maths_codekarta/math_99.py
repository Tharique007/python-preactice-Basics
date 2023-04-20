A=int(input(":"))
list1=[int(n) for n in input().split(" ",A-1)]
value=1
max_of_list=max(list1)
index_of_max= list1.index(max_of_list)
if index_of_max == 0:
    print(value)
else:
    high=list1[0]
    for i in range(1,index_of_max+1):
        if list1[i]>high:
            value += 1
            high = list1[i]
        elif list1[i] == high or list1[i] < high:
            continue
    print(value)