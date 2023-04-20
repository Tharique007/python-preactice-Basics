a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
gcd1 =list1[0]
from math import gcd
for i in range(1,a):
    gcd1 = gcd(gcd1,list1[i])
if gcd1 > 0:
    print(gcd1)
else:
    print(-1)