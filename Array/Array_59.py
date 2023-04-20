a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
output_index=[]
output=[]
if list1.count(0) > 1:
    for i in range(0,a):
        if list1[i] ==0:
            output_index.append(i)
    print(*output_index)
    for i in range(0,len(output_index)-1):
        for j in range(output_index[i]+1,output_index[i+1]):
            output.append(list1[j])
    print(*output)
else:
    print(-1)