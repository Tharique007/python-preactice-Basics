"""
Check whether the given 4 points form a square or not.
Example:
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes
"""

x_list=[]
y_list=[]
result_list1=[]
result_list2=[]
from math import sqrt
for i in range (0,4):
    x=str(i+1)
    a,b = input("enter the"+x+" points ").split()
    x_list.append(int(a))
    y_list.append(int(b))
for i in range (0,4):
    a1=x_list[i]
    b1=y_list[i]
    if i<3:
        a2=x_list[i+1]
        b2=y_list[i+1]
    elif i==3:
        a2 = x_list[i-3]
        b2 = y_list[i-3]
    result = ((a2-a1)**2)+((b2-b1)**2)
    result_list1.append(sqrt(result))
print(result_list1)

for i in range(0,2):
    a1 = x_list[i]
    b1 = y_list[i]
    a2 = x_list[i+2]
    b2 = y_list[i+2]
    result = ((a2-a1)**2)+((b2-b1)**2)
    result_list2.append(sqrt(result))
print(result_list2)

if result_list1[0] == result_list1[1] == result_list1[2] == result_list1[3] != 0 and result_list1[0] == result_list1[1] == result_list1[2] == result_list1[3]:
    if result_list2[0] == result_list2[1]:
        print("yes")
    else:
        print("no")
else:
        print("no")

