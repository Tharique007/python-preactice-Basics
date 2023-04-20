a,b=map(int,input(":").split(" "))
vala=1
for i in range(1,a+1):
    vala *= i
valb=1
for i in range(1,b+1):
    valb *= i
ans=int(vala/valb)
print(ans)