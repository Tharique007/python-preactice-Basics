"""
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
"""
a1,b1=str(input()).split(" ")
a=int(a1)
b=int(b1)
count = -1
list_in=[int(num) for num in input().split(" ",a-1)]
for i in list_in:
    if i == b:
        count += 1
print(count)