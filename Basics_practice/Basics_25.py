"""
Write a code to get 2 integers as input and add the integers without any carry.

Input Description:
A single line containing 2 integers.

Output Description:
Print sum of the 2 integers without carry

Sample Input :
44 66
Sample Output :
0
"""


a1,b2=str(input("Enter the two number")).split(" ")
a= int(a1)
b= int(b2)
string =""


while (a//10)>0 and (b//10)>0:
    if a>9 and b>9:
        c = (a%10)+(b%10)
        if c>9:
            string = string + str(c%10)
        else:
            string = string + str(c)
        a= a//10
        b= b//10


if (a+b) > 9:
    string = string + str((a+b)%10)
else:
    string = string + str((a + b))


print(int(string[::-1]))




