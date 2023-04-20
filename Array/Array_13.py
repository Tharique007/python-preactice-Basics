a,n=map(int,input().split(" ",2-1))
list1=[int(num) for num in input().split(" ",a-1)]
output=""
for i in range(0,len(list1)):
    if list1[i] == n:
        output = output + str(i+1)+" "
if len(output)>=1:
    print(output.rstrip())
else:
    print(-1)