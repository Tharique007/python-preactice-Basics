"""
Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
Input Size N <= 100000
Sample Testcase :
INPUT
4
4 3 2 1
OUTPUT
0
"""

a=int(input())
list_1=[int(num) for num in input().split(" ",a-1)]
res = list_1[0]

for i in range(1,len(list_1)):
    res = res & list_1[i]

print(res)