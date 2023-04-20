a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
multi=1
output=[]
for i in listin:
    multi *= i

for i in listin:
    num = int(multi/i)
    output.append(num)
print(*output)