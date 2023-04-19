"""
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd
"""

a1,b1 = str(input()).split(" ")
a= int(a1)
b= int(b1)
c= a+b
if c%2 == 0:
    print("even")
else:
    print("odd")