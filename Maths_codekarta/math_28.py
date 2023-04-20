a=int(input(":"))
listout=[]
counter = 0
for i in range(1,(a+1)):
    counter += i
    listout.append((counter**2))
print(*listout)
