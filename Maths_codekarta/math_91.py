from math import gcd
def GCD_ofThreenumber(a,b,c):
    x= gcd(a,b)
    return gcd(x,c)

input1 = int(input(":"))
result = False
output=[]
for i in range(1,input1+1):
    process = input1-i
    for j in range(1,process+1):
        k=process-j
        if GCD_ofThreenumber(i,j,k) == 1:
            output.append(i)
            output.append(j)
            output.append(k)
            output.sort()
            print(output)
            result = True
            break
    if result:
        break
if result == False:
    print(0)


