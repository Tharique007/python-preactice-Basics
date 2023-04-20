a=int(input(":"))
listin = [int(num) for num in input().split(" ",a-1)]
output1=0
for i in listin:
    if i <0:
        output1= output1 + i
print(output1)