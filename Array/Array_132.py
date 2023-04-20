a=int(input(":"))
outlist=[]

def isprimenumber(num: int)->bool:
    if num<= 1 :
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for i in range(2,a):
    #print(i)
    if isprimenumber(i) and a%i == 0:
        b=int(a/i)
        #print("ii:", i,b)
        #print(isprimenumber(b))
        if isprimenumber(b) and i != b:
            if i and b not in outlist:
                outlist.append(i)
                outlist.append(b)
outlist.sort(reverse=True)
if len(outlist) >0:
    print(*outlist)
else:
    print(-1)