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
if primenumber(a):
    print("yes")
else:
    print("no")

