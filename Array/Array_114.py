l,r=map(int,input(":").split(" "))
number= 2
resut = True

while(resut == True):
    if number%l == 0 and number%r == 0:
        resut =False
        print(number)
    else:
        number += 1
