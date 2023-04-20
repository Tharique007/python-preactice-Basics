a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
output=[]

for i in range(0,len(listin)):

    if i%2 == 0:
        if listin[i]%2 !=0:
            output.append(listin[i])
    elif i%2 != 0:
        if listin[i] %2 == 0:
            output.append(listin[i])

if len(output) > 0:
    print(*output)
else:
    print(-1)