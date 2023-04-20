"""
Given base(B) and height(H) of a triangle find its area.
Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4
"""


B,H =map(int, input("enter B and H value").split(" "))
# base=int(B)
# Height=int(H)

print(int(0.5*B*H))