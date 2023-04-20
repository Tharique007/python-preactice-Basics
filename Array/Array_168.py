a= int(input(":"))
output=[]

def factorila(num1):
    numefact = 1
    for i in range(1, (num1+1)):
        numefact = numefact * i
    return numefact

def cathlonnnum(num):
    twiceN= factorila((2*num))
    Nplus1= factorila((num+1))
    Nfactorial=factorila(num)
    denominator = Nplus1*Nfactorial
    result = int(twiceN/denominator)
    return result


for i in range(0,(a+1)):
    output.append(cathlonnnum(i))
print(*output)
