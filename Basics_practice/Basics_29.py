"""
Given a number N and an array of N elements, find the Bitwise OR of the array elements.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
"""



a=int(input("enter the length of the array"))
list_in = [int(num) for num in input().split(" ",a-1)]
#print(list_in)
result = list_in[0]
for i in range(1,len(list_in)):
    result = result | list_in[i]
print(result)