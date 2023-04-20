def primenumber(num):
    if num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num>3:
        count=0
        for i in range(1,num+1):
            if count <= 2:
                if num %i == 0:
                    count +=1
            else:
                return False
        if count == 2:
            return True
a=int(input(":"))
factorlist=[]
primefactorlist=[]
if primenumber(a):
    for i in range(1,a+1):
        if a % i ==0:
            factorlist.append(i)
            #factorlist.append(int(a/i))
else:
    for i in range(1,a+1):
        if a % i ==0:
            factorlist.append(i)
            factorlist.append(int(a/i))
#print(factorlist)

for  j in factorlist:
    if primenumber(j):
        primefactorlist.append(j)
#print(primefactorlist)
print(len(primefactorlist))