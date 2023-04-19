"""
Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
Sample Testcase :
INPUT
3
2 6
OUTPUT
yes
"""

a=int(input("enter a number"))
b_1,c_1 = str(input("enter two numbers: ")).split(" ")
b= int(b_1)
c=int(c_1)
if a in range (b,c):
    print("yes")
else:
    print("no")
