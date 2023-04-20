a=int(input("Enter the length of array"))
list_1 = [int(num) for num in input().split(" ",a-1)]
out_1=""
for i in range(0,(len(list_1))):
    count=0
    for j in range((i+1),(len(list_1))):
        if list_1[j]<list_1[i]:
            out_1=out_1+str(list_1[j])+" "
            count += 1
            break;
    if count == 0:
        out_1 = out_1 + "-1" + " "
print(a)
print(out_1.rstrip())
