a=int(input(":"))
primefactor=[]
factors=[]

for i in range(2,a+1):
    if a%i == 0:
        factors.append(i)
for i in factors:
    count=0
    for j in range(1,i):
        if count < 2:
            if i%j == 0:
                count += 1
        else:
            break
    if count<2:
        primefactor.append(i)
print(*primefactor)
