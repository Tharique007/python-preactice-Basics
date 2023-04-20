a=int(input(":"))
def primenumber(number):
    if (number <2):
        return False
    if (number == 2 or number == 3):
        return True
    else:
        count=0
        for i in range(1,number+1):
            #print(i)
            if count <=2:
                if (number%i) == 0:
                    count +=1
            elif count>2:
                return False
                break
        #print(count)
        if count <= 2:
            return True
number_of_prime = 1
value=0
start = 2
listout=[]
while number_of_prime <= a:
    if primenumber(start):
        number_of_prime +=1
        value += start
        listout.append(value)
    start +=1

print(*listout)





