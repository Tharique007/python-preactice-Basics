a=int(input(":"))
factorslist=[]
outputlist=[]
def findifprime(num):
    if num <= 1:
        return False
    if num==2 or num == 3:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for i in range(2,100):
    if a%i == 0 and i not in factorslist:
        factorslist.append(i)
for j in factorslist:
    if findifprime(j):
        outputlist.append(j)
outputlist.sort()
print(*outputlist)