"""
Write a code to get an integer N and print the digits of the integer.

Input Description:
A single line contains an integer N.

Output Description:
Print the digits of the integer in a single line separated by space,

Sample Input :
348
Sample Output :
3 4 8
"""

a=int(input())
b=str(a)
c=""
for i in b:
    c=c+i+" "
print(c.rstrip())