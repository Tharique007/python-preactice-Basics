string,a=input(":").split(" ")
a= int(a)
output=""
for i in range(a-1,len(string),a):
    print("i:",i)
    output += string[i]+" "
print(output.rstrip())
