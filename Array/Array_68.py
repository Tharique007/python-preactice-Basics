input1=input(":")
output=""

for i in input1:
    j = ord(i)
    print(j)
    if (j+3 > 90 and j+3<97) or j+3>122:
        output += chr((j+3)-26)
    else:
        output += chr((j+3))
print(output)