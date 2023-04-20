inputstr=input(":")
listin=inputstr.split(" ")
output=""
for i in listin:
    output += i[0]
    if len(i)>2:
        for j in range(-2,-len(i),-1):
            output += i[j]
        output += i[len(i) - 1]
    elif len(i)==2:
        output += i[len(i) - 1]

    output += " "

print(output.rstrip())