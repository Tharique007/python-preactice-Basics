"""
Given a number N, print 'yes' if it is composite else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
yes
"""

input_in = int(input("Enter the number"))
count=0
for i in range(1,(input_in+1)):
    if input_in % i == 0:
            count += 1
if count <3:
    print("no")
else:
    print("yes")