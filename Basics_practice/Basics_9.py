"""
Find the minimum among 10 numbers.
Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1
"""

input_= str(input())
input_list = input_.split(" ")
a = int(input_list[0])
for i in input_list:
    if (int(i)<a):
        a = int(i)
print(a)