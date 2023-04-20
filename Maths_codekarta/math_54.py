inn=int(input(":"))
from math import gcd
def stiff_number(a):
    if a%2 == 0:
        c= (int(a/2)+1)
    elif a%2 != 0:
        c= (int(a/2)+2)
    for i in range(2,c):
        b=a-i
        if gcd(i,b) == 1:
            return True
    return False
if stiff_number(inn):
    print("Stiff")
else:
    print("not")