a=int(input(":"))
listouter=[0]*a
output=""
for i in range(0,a):
    b=int(input())
    listouter[i]=[int(num) for num in input().split(" ",(b-1))]

for i in listouter:
    i.sort()
    for j in i:
        output = output + str(j)+" "
#print(listouter)
print(output.rstrip())