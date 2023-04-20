string=input(":")
liststring=string.split(" ")
output=""
for i in liststring:
    output += i[::-1]+" "
print(output.rstrip())