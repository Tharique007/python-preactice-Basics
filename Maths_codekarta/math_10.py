input_= str(input("enter the number: "))
input_list = input_.split(" ")
a = int(input_list[0])
for i in input_list:
    if (int(i)<a):
        a = int(i)
print(a)
