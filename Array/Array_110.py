a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
from math import gcd

lcm = 1
for i in list1:
    lcm = int((lcm * i)/gcd(lcm,i))
print(lcm)