a=int(input(":"))
output=[]
for i in range(2,a+1):
    if a%i==0 and i%2 == 0:
        output.append(i)
if len(output) >0:
    print(*output)
else:
    print(-1)