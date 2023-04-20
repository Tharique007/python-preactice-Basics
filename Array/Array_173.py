inut1=input(":")
listin=inut1.split(" ")
output=""
for i in listin:
    output += i[::-1] + " "
print(output.rstrip())
