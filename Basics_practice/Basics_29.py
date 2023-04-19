a=int(input("enter the length of the array"))
list_in = [int(num) for num in input().split(" ",a-1)]
#print(list_in)
result = list_in[0]
for i in range(1,len(list_in)):
    result = result | list_in[i]
print(result)