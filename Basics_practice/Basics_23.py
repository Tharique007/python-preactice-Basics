"""
Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
Sample Testcase :
INPUT
10 5
OUTPUT
5
"""


a1,b1 = str(input("enter twwo numbers")).split()
a = abs(int(a1))
b = abs(int(b1))
print(a)
print(b)
small=0
big=0
result=1
if a != 0 and b != 0:
    if a > b:
        small = b
        big = a
    else:
        small = a
        big = b

    while result != 0:
        result = big % small
        big = small
        small = result
    print(big)

else:
    print("-1")