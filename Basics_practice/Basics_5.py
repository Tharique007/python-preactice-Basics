"""
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
"""


from math import sqrt
a,b= str(input("enter the two numbers: ")).split(" ")
c=int(a)
d=int(b)
product = c*d
sqr_root=sqrt(product)
# print(sqr_root)
# print(type(sqr_root))

list_sqrt=str(sqr_root).split(".")
print(list_sqrt)
if len(list_sqrt[1]) >1:
    print("no")
elif int(list_sqrt[1]) >0:
    print("no")
else:
    print("yes")