"""
Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7
"""

A= int(input())
B= 0
C= str(A)
for i in C:
    B= B+int(i)
print(B)