input_=input()

in_list=input_.split(" ")

a=float(in_list[0])

b=float(in_list[1])

c=float(in_list[2])

ac4=(a*c*4)

bsq=(b*b)

val=(bsq-ac4)

from math import sqrt

x1=(((-b)+sqrt(val))/(2*a))
x2=(((-b)-sqrt(val))/(2*a))

x1_format = "{:.2f}".format(int(x1))
x2_format = "{:.2f}".format(x2)

print(x1_format)
print(x2_format)
print(type(x1_format))
print(type(x2_format))