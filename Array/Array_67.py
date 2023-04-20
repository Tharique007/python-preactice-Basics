input1=input(":")
input1=input1.strip(" ")
output=""
for i in range(0,(len(input1))):
    if input1[i] == " " and input1[i+1]==" ":
        pass
    else:
        output += input1[i]

print(output)
