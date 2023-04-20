input_1 = int(input("Enter the number"))
input_2 = str(input_1)
count = 0
for i in input_2:
    count = count+int(i)
print(count)
if (count%3 == 0):
    print("yes")
else:
    print("not")
