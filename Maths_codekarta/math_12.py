n=int(input("enter the number of element: "))
list_1 =[int(num) for num in input().split(" ",(n-1))]
small = list_1[0]
for i in range (0 ,len(list_1)):
    if (list_1[i] < small):
        small=list_1[i]
print(small)