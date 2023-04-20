a=int(input(":"))

def nthHypenumber(numn):
    count=0
    list1=[2,3,5,7]
    num = 2
    while count < numn:
        rep = 0
        for i in str(num):
            if int(i) not in list1:
                num +=1
                break
            else:
                rep +=1
        if rep == len(str(num)):
            count += 1
            if count != numn:
                num +=1

    return num
print(nthHypenumber(a))

