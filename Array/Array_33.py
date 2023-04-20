a= int(input(":"))
odd=1
for i in range(1,(a+1)):
    output1 = ""
    for j in range(0,odd):
        output1 = output1+ "1"+" "
    odd = odd+2
    print(output1.rstrip())
