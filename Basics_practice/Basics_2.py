"""
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes
"""


c,d = str(input("enter two numbers:")).split(" ")
a=int(c)
b=(int(d))
input_list=[int(num) for num in input().split(" ", (a-1))]
if input_list.count(b) != 0:
        print("yes")
else:
    print("no")
