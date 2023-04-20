print("Enter the length of the List")
list_len=int(input(""))
print("Enter the list elments")
list_in=[int(i) for i in input().split(" ",list_len-1)]
sum1=0
for j in list_in:
    sum1 += j
print(sum1)

#or

print(sum(list_in))