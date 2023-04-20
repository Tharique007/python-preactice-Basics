a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
totalcount=0

for i in range(0,a-1):
    count = 1
    for j in range(i,a-1):
        if listin[j+1] > listin[j]:
            count += 1
            #print("i",i, "j",j, "couunt" , count)
        else:
            break
    #print(count)
    if count > totalcount:
        totalcount = count
if totalcount > 1:
    print(totalcount)
else:
    print(-1)


