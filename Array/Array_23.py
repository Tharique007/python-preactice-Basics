a=int(input(":"))
listin=[int(num) for num in input().split(" ",a-1)]
w=int(input("w:"))
output=""

for i in range(0,(len(listin)-(w-1))):
    count=0
    for j in range(i,(i+w)):
        if listin[j] <0:
            count +=1
            output = output + str(listin[j])+" "
            break
    if count == 0:
        output = output + "0" + " "
print(output.rstrip())